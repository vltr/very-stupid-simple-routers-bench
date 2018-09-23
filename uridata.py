import itertools
import random
from enum import IntEnum


class ParamFormat(IntEnum):
    ROUTES = 1
    KUA = 2
    XRTR = 3
    SANIC = 4
    FALCON = 5


def get_part_formatter(param_format):
    if param_format in (ParamFormat.ROUTES, ParamFormat.FALCON):
        return uri_type_two
    elif param_format in (ParamFormat.KUA, ParamFormat.XRTR):
        return uri_type_three
    elif param_format == ParamFormat.SANIC:
        return uri_type_one


def format_uri(parts):
    return "/{}".format("/".join(parts))


def format_dynamic_uri(parts, prefix, param_format):
    f = get_part_formatter(param_format)
    np = []
    i = 1
    for p in parts:
        if p == "*":
            np.append(f("{}_{}".format(prefix, i)))
            i += 1
        else:
            np.append(p)
    return "/{}".format("/".join(np))


def populate_dynamic_uri(parts, values):
    np = []
    i = 0
    for p in parts:
        if p == "*":
            np.append(values[i])
            i += 1
        else:
            np.append(p)
    return "/{}".format("/".join(np))


def uri_type_one(part):
    return "<%s>" % part


def uri_type_two(part):
    return "{%s}" % part


def uri_type_three(part):
    return ":%s" % part


def generate_dynamic_uri(data, n_vars=1):
    n = int(len(data) / 2) - 1
    pos = random.randint(max(2, n_vars + 1), n + n_vars)
    idx = sorted(random.sample(range(2, pos + 1), n_vars))
    uri = list(random.sample(list(itertools.combinations(data, pos)), 1)[0])
    for i in idx:
        uri[i - 1] = "*"
    return uri


def full_combinations(data, n=0):
    if n == 0:
        n = int(len(data) / 2)
    for i in range(n):
        if i == 0:
            continue
        for c in itertools.combinations(data, i):
            yield c


# taken from https://docs.python.org/3/library/itertools.html#itertools-recipes
def random_combination(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    indices = sorted(random.sample(range(n), r))
    return tuple(pool[i] for i in indices)


def should_avoid(p, avoid):
    for a in avoid:
        if p[: len(a)] == a:
            return True
    return False


def generate_test_uris(data, avoid):
    uris = []
    s = int(len(data) / 2)
    for p in full_combinations(data, s):
        p = list(p)
        if should_avoid(p, avoid):
            continue
        uris.append(p)
    return uris


_WORDS = [  # random words just to create some fake URLs
    "company",
    "user",
    "domain",
    "posts",
    "list",
    "search",
    "api",
    "auth",
    "register",
    "products",
    "fetch",
]


class SimpleData:
    def __init__(self, data=None):
        if data is None:
            data = _WORDS
        self.generate_all(data)

    def generate_all(self, data):
        self.one_var_uri = ["a", "*"]
        self.two_var_uri = ["b", "*", "*"]
        self.three_var_uri = ["c", "*", "*", "*"]
        self.zero_var_uri = format_uri(["d", "c", "b", "a"])
        self.static_uris = []

    def get_static_uris(self):
        for p in self.static_uris:
            yield format_uri(p)

    def get_zero_var_uri(self, param_format=ParamFormat.SANIC):
        return self.zero_var_uri

    def get_one_var_uri(self, param_format=ParamFormat.SANIC):
        return format_dynamic_uri(self.one_var_uri, "one", param_format)

    def get_two_var_uri(self, param_format=ParamFormat.SANIC):
        return format_dynamic_uri(self.two_var_uri, "one", param_format)

    def get_three_var_uri(self, param_format=ParamFormat.SANIC):
        return format_dynamic_uri(self.three_var_uri, "one", param_format)

    def populate_zero_var_uri(self, *values):
        return self.zero_var_uri

    def populate_one_var_uri(self, *values):
        return populate_dynamic_uri(self.one_var_uri, values)

    def populate_two_var_uri(self, *values):
        return populate_dynamic_uri(self.two_var_uri, values)

    def populate_three_var_uri(self, *values):
        return populate_dynamic_uri(self.three_var_uri, values)


class BenchData(SimpleData):
    def generate_all(self, data):
        one_var_uri = generate_dynamic_uri(data, 1)
        two_var_uri = generate_dynamic_uri(data, 2)
        three_var_uri = generate_dynamic_uri(data, 3)

        while (
            one_var_uri[0] == two_var_uri[0]
            or one_var_uri[0] == three_var_uri[0]
            or two_var_uri[0] == three_var_uri[0]
        ):
            # this is lazy, i know
            one_var_uri = generate_dynamic_uri(data, 1)
            two_var_uri = generate_dynamic_uri(data, 2)
            three_var_uri = generate_dynamic_uri(data, 3)

        self.one_var_uri = one_var_uri
        self.two_var_uri = two_var_uri
        self.three_var_uri = three_var_uri

        one_var_start = one_var_uri[: one_var_uri.index("*")]
        two_var_start = two_var_uri[: two_var_uri.index("*")]
        three_var_start = three_var_uri[: three_var_uri.index("*")]

        self.static_uris = generate_test_uris(
            data, avoid=[one_var_start, two_var_start, three_var_start]
        )

        self.zero_var_uri = random.choice(self.static_uris)
        del self.static_uris[self.static_uris.index(self.zero_var_uri)]
        self.zero_var_uri = format_uri(self.zero_var_uri)
