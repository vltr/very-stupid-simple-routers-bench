import argparse
import random
import sys
import timeit
import uuid

import kua
import matplotlib.pyplot as plt
from falcon.routing import CompiledRouter
from routes import Mapper
from sanic.router import Router
from xrtr import RadixTree

from extras import Endpoint
from extras import res_factory
from uridata import BenchData
from uridata import ParamFormat
from uridata import SimpleData

_IMP_STMT = """import random
import uuid
from __main__ import {}
from __main__ import minimal_uris
from __main__ import lots_of_uris

def gen_int():
    return str(random.randint(1000, 9999))

def gen_uuid():
    return str(uuid.uuid4())

"""


def create_bench_data():
    return SimpleData(), BenchData()


def gen_int():
    return str(random.randint(1000, 9999))


def gen_uuid():
    return str(uuid.uuid4())


def print_type_of_test(msg):
    print("----------------------------------------")
    print(msg)


def gen_stmt(router_call, uris, nvars, complex, is_sanic=False, is_xrtr=False):
    if complex:
        params = ["gen_uuid()"] * nvars
    else:
        params = ["gen_int()"] * nvars
    if nvars == 0:
        fn = "populate_zero_var_uri"
    elif nvars == 1:
        fn = "populate_one_var_uri"
    elif nvars == 2:
        fn = "populate_two_var_uri"
    elif nvars == 3:
        fn = "populate_three_var_uri"
    if is_xrtr:
        return "{}({}.{}({}), 'GET')".format(
            router_call, uris, fn, ", ".join(params)
        )
    if is_sanic:
        return "{}({}.{}({}), 'GET', '')".format(
            router_call, uris, fn, ", ".join(params)
        )
    return "{}({}.{}({}))".format(router_call, uris, fn, ", ".join(params))


def measure_router(router_name, run_stmt, times):
    imp_stmt = _IMP_STMT.format(router_name)

    print("BENCHMARKING ROUTER: %s" % router_name)
    # print('> %s' % imp_stmt)
    print("> %s" % run_stmt)

    time_to_run = timeit.timeit(run_stmt, setup=imp_stmt, number=times)
    time_each = time_to_run / times
    print(
        "%s: %d results in %f s (%f per sec)"
        % (router_name, times, time_to_run, 1. / time_each)
    )
    print("")
    return time_to_run, (1. / time_each)


def create_falcon_router(uri_data):
    router = CompiledRouter()
    # static routes
    for u in uri_data.get_static_uris():
        res = res_factory(u, ["GET"])
        router.add_route(u, method_map=None, resource=res)

    # zero variable
    template = uri_data.get_zero_var_uri(ParamFormat.FALCON)
    res = res_factory(template, ["GET"])
    router.add_route(template, method_map=None, resource=res)
    # one variable
    template = uri_data.get_one_var_uri(ParamFormat.FALCON)
    res = res_factory(template, ["GET"])
    router.add_route(template, method_map=None, resource=res)
    # two variables
    template = uri_data.get_two_var_uri(ParamFormat.FALCON)
    res = res_factory(template, ["GET"])
    router.add_route(template, method_map=None, resource=res)
    # three variables
    template = uri_data.get_three_var_uri(ParamFormat.FALCON)
    res = res_factory(template, ["GET"])
    router.add_route(template, method_map=None, resource=res)
    # done
    return router


def create_kua_router(uri_data):
    endpoint = Endpoint("kua")
    router = kua.Routes()
    # static routes
    for u in uri_data.get_static_uris():
        router.add(u, {"GET": endpoint})

    # zero variable
    template = uri_data.get_zero_var_uri(ParamFormat.KUA)
    router.add(template, {"GET": endpoint})
    # one variable
    template = uri_data.get_one_var_uri(ParamFormat.KUA)
    router.add(template, {"GET": endpoint})
    # two variables
    template = uri_data.get_two_var_uri(ParamFormat.KUA)
    router.add(template, {"GET": endpoint})
    # three variables
    template = uri_data.get_three_var_uri(ParamFormat.KUA)
    router.add(template, {"GET": endpoint})
    # done
    return router


def create_routes_router(uri_data):
    endpoint = Endpoint("routes")
    router = Mapper()
    # static routes
    for u in uri_data.get_static_uris():
        router.connect(None, u, controller=endpoint)

    # zero variable
    template = uri_data.get_zero_var_uri(ParamFormat.ROUTES)
    router.connect(None, template, controller=endpoint)
    # one variable
    template = uri_data.get_one_var_uri(ParamFormat.ROUTES)
    router.connect(None, template, controller=endpoint)
    # two variables
    template = uri_data.get_two_var_uri(ParamFormat.ROUTES)
    router.connect(None, template, controller=endpoint)
    # three variables
    template = uri_data.get_three_var_uri(ParamFormat.ROUTES)
    router.connect(None, template, controller=endpoint)
    # done
    return router


def create_sanic_router(uri_data):
    endpoint = Endpoint("sanic")
    router = Router()
    # static routes
    for u in uri_data.get_static_uris():
        router.add(u, methods=["GET"], handler=endpoint)

    # zero variable
    template = uri_data.get_zero_var_uri(ParamFormat.SANIC)
    router.add(template, methods=["GET"], handler=endpoint)
    # one variable
    template = uri_data.get_one_var_uri(ParamFormat.SANIC)
    router.add(template, methods=["GET"], handler=endpoint)
    # two variables
    template = uri_data.get_two_var_uri(ParamFormat.SANIC)
    router.add(template, methods=["GET"], handler=endpoint)
    # three variables
    template = uri_data.get_three_var_uri(ParamFormat.SANIC)
    router.add(template, methods=["GET"], handler=endpoint)
    # done
    return router


def create_xrtr_router(uri_data):
    endpoint = Endpoint("xrtr")
    router = RadixTree()
    # static routes
    for u in uri_data.get_static_uris():
        router.insert(u, endpoint, ["GET"])

    # zero variable
    template = uri_data.get_zero_var_uri(ParamFormat.XRTR)
    router.insert(template, endpoint, ["GET"])
    # one variable
    template = uri_data.get_one_var_uri(ParamFormat.XRTR)
    router.insert(template, endpoint, ["GET"])
    # two variables
    template = uri_data.get_two_var_uri(ParamFormat.XRTR)
    router.insert(template, endpoint, ["GET"])
    # three variables
    template = uri_data.get_three_var_uri(ParamFormat.XRTR)
    router.insert(template, endpoint, ["GET"])
    # done
    return router


def main():
    # ----------------------------------------------------------------------- #
    # creating arg parser
    # ----------------------------------------------------------------------- #
    parser = argparse.ArgumentParser(
        description="Performs the benchmark of several routing systems in Python, both from frameworks or standalone solutions"
    )
    parser.add_argument(
        "--skip-falcon",
        action="store_true",
        help="skip Falcon from the benchmark",
        dest="skip_falcon",
        default=False,
    )
    parser.add_argument(
        "--skip-kua",
        action="store_true",
        help="skip kua from the benchmark",
        dest="skip_kua",
        default=False,
    )
    parser.add_argument(
        "--skip-routes",
        action="store_true",
        help="skip Routes from the benchmark",
        dest="skip_routes",
        default=False,
    )
    parser.add_argument(
        "--skip-sanic",
        action="store_true",
        help="skip Sanic from the benchmark",
        dest="skip_sanic",
        default=False,
    )
    parser.add_argument(
        "--skip-xrtr",
        action="store_true",
        help="skip xrtr from the benchmark",
        dest="skip_xrtr",
        default=False,
    )
    parser.add_argument(
        "--plot",
        action="store_true",
        help="plot the results using matplotlib",
        dest="plot",
        default=True,
    )
    parser.add_argument(
        "--iters",
        type=int,
        help="number of iterations on each test",
        dest="total_iter",
        default=100000,
    )
    try:
        args = parser.parse_args()
    except Exception:
        parser.print_help()
        sys.exit(1)
    # ----------------------------------------------------------------------- #
    # start testing
    # ----------------------------------------------------------------------- #
    print("\n==========================================")
    print("THIS TEST CAN TAKE A WHILE ...")
    print("==========================================\n")

    res = {
        "falcon": {
            "min": {"simple": {}, "complex": {}},
            "full": {"simple": {}, "complex": {}},
        },
        "kua": {
            "min": {"simple": {}, "complex": {}},
            "full": {"simple": {}, "complex": {}},
        },
        "routes": {
            "min": {"simple": {}, "complex": {}},
            "full": {"simple": {}, "complex": {}},
        },
        "sanic": {
            "min": {"simple": {}, "complex": {}},
            "full": {"simple": {}, "complex": {}},
        },
        "xrtr": {
            "min": {"simple": {}, "complex": {}},
            "full": {"simple": {}, "complex": {}},
        },
    }

    global falcon_compiled_router_minimal
    global falcon_compiled_router_full
    global kua_router_minimal
    global kua_router_full
    global routes_router_minimal
    global routes_router_full
    global sanic_router_minimal
    global sanic_router_full
    global xrtr_router_minimal
    global xrtr_router_full
    global minimal_uris
    global lots_of_uris

    minimal_uris, lots_of_uris = create_bench_data()
    num_vars = ["ZERO", "ONE", "TWO", "THREE"]

    # ----------------------------------------------------------------------- #
    if not args.skip_falcon:

        falcon_compiled_router_minimal = create_falcon_router(minimal_uris)

        for i, k in enumerate(num_vars):

            print_type_of_test(
                "MINIMAL, {} VARIABLE, SIMPLE STRING, NO-REPEAT".format(k)
            )
            run_stmt = gen_stmt(
                "falcon_compiled_router_minimal.find", "minimal_uris", i, False
            )
            res["falcon"]["min"]["simple"][k] = measure_router(
                "falcon_compiled_router_minimal", run_stmt, args.total_iter
            )

            print_type_of_test(
                "MINIMAL, {} VARIABLE, COMPLEX STRING, NO-REPEAT".format(k)
            )
            run_stmt = gen_stmt(
                "falcon_compiled_router_minimal.find", "minimal_uris", i, True
            )
            res["falcon"]["min"]["complex"][k] = measure_router(
                "falcon_compiled_router_minimal", run_stmt, args.total_iter
            )

        # ------------------------------------------------------------------- #
        falcon_compiled_router_full = create_falcon_router(lots_of_uris)

        for i, k in enumerate(num_vars):

            print_type_of_test(
                "FULL, {} VARIABLE, SIMPLE STRING, NO-REPEAT".format(k)
            )
            run_stmt = gen_stmt(
                "falcon_compiled_router_full.find", "lots_of_uris", i, False
            )
            res["falcon"]["full"]["simple"][k] = measure_router(
                "falcon_compiled_router_full", run_stmt, args.total_iter
            )

            print_type_of_test(
                "FULL, {} VARIABLE, COMPLEX STRING, NO-REPEAT".format(k)
            )
            run_stmt = gen_stmt(
                "falcon_compiled_router_full.find", "lots_of_uris", i, True
            )
            res["falcon"]["full"]["complex"][k] = measure_router(
                "falcon_compiled_router_full", run_stmt, args.total_iter
            )

    # ----------------------------------------------------------------------- #
    if not args.skip_kua:

        kua_router_minimal = create_kua_router(minimal_uris)

        for i, k in enumerate(num_vars):

            print_type_of_test(
                "MINIMAL, {} VARIABLE, SIMPLE STRING, NO-REPEAT".format(k)
            )
            run_stmt = gen_stmt(
                "kua_router_minimal.match", "minimal_uris", i, False
            )
            res["kua"]["min"]["simple"][k] = measure_router(
                "kua_router_minimal", run_stmt, args.total_iter
            )

            print_type_of_test(
                "MINIMAL, {} VARIABLE, COMPLEX STRING, NO-REPEAT".format(k)
            )
            run_stmt = gen_stmt(
                "kua_router_minimal.match", "minimal_uris", i, True
            )
            res["kua"]["min"]["complex"][k] = measure_router(
                "kua_router_minimal", run_stmt, args.total_iter
            )

        # ------------------------------------------------------------------- #
        kua_router_full = create_kua_router(lots_of_uris)

        for i, k in enumerate(num_vars):

            print_type_of_test(
                "FULL, {} VARIABLE, SIMPLE STRING, NO-REPEAT".format(k)
            )
            run_stmt = gen_stmt(
                "kua_router_full.match", "lots_of_uris", i, False
            )
            res["kua"]["full"]["simple"][k] = measure_router(
                "kua_router_full", run_stmt, args.total_iter
            )

            print_type_of_test(
                "FULL, {} VARIABLE, COMPLEX STRING, NO-REPEAT".format(k)
            )
            run_stmt = gen_stmt(
                "kua_router_full.match", "lots_of_uris", i, True
            )
            res["kua"]["full"]["complex"][k] = measure_router(
                "kua_router_full", run_stmt, args.total_iter
            )

    # ----------------------------------------------------------------------- #
    if not args.skip_routes:

        routes_router_minimal = create_routes_router(minimal_uris)

        for i, k in enumerate(num_vars):

            print_type_of_test(
                "MINIMAL, {} VARIABLE, SIMPLE STRING, NO-REPEAT".format(k)
            )
            run_stmt = gen_stmt(
                "routes_router_minimal.match", "minimal_uris", i, False
            )
            res["routes"]["min"]["simple"][k] = measure_router(
                "routes_router_minimal", run_stmt, args.total_iter
            )

            print_type_of_test(
                "MINIMAL, {} VARIABLE, COMPLEX STRING, NO-REPEAT".format(k)
            )
            run_stmt = gen_stmt(
                "routes_router_minimal.match", "minimal_uris", i, True
            )
            res["routes"]["min"]["complex"][k] = measure_router(
                "routes_router_minimal", run_stmt, args.total_iter
            )

        # ------------------------------------------------------------------- #
        routes_router_full = create_routes_router(lots_of_uris)  # THIS IS SLOW

        for i, k in enumerate(num_vars):

            print_type_of_test(
                "FULL, {} VARIABLE, SIMPLE STRING, NO-REPEAT".format(k)
            )
            run_stmt = gen_stmt(
                "routes_router_full.match", "lots_of_uris", i, False
            )
            res["routes"]["full"]["simple"][k] = measure_router(
                "routes_router_full", run_stmt, args.total_iter
            )

            print_type_of_test(
                "FULL, {} VARIABLE, COMPLEX STRING, NO-REPEAT".format(k)
            )
            run_stmt = gen_stmt(
                "routes_router_full.match", "lots_of_uris", i, True
            )
            res["routes"]["full"]["complex"][k] = measure_router(
                "routes_router_full", run_stmt, args.total_iter
            )

    # ----------------------------------------------------------------------- #
    if not args.skip_sanic:

        sanic_router_minimal = create_sanic_router(minimal_uris)

        for i, k in enumerate(num_vars):

            print_type_of_test(
                "MINIMAL, {} VARIABLE, SIMPLE STRING, NO-REPEAT".format(k)
            )
            run_stmt = gen_stmt(
                "sanic_router_minimal._get",
                "minimal_uris",
                i,
                False,
                is_sanic=True,
            )
            res["sanic"]["min"]["simple"][k] = measure_router(
                "sanic_router_minimal", run_stmt, args.total_iter
            )

            print_type_of_test(
                "MINIMAL, {} VARIABLE, COMPLEX STRING, NO-REPEAT".format(k)
            )
            run_stmt = gen_stmt(
                "sanic_router_minimal._get",
                "minimal_uris",
                i,
                True,
                is_sanic=True,
            )
            res["sanic"]["min"]["complex"][k] = measure_router(
                "sanic_router_minimal", run_stmt, args.total_iter
            )

        # ------------------------------------------------------------------- #
        sanic_router_full = create_sanic_router(lots_of_uris)

        for i, k in enumerate(num_vars):

            print_type_of_test(
                "FULL, {} VARIABLE, SIMPLE STRING, NO-REPEAT".format(k)
            )
            run_stmt = gen_stmt(
                "sanic_router_full._get",
                "lots_of_uris",
                i,
                False,
                is_sanic=True,
            )
            res["sanic"]["full"]["simple"][k] = measure_router(
                "sanic_router_full", run_stmt, args.total_iter
            )

            print_type_of_test(
                "FULL, {} VARIABLE, COMPLEX STRING, NO-REPEAT".format(k)
            )
            run_stmt = gen_stmt(
                "sanic_router_full._get",
                "lots_of_uris",
                i,
                True,
                is_sanic=True,
            )
            res["sanic"]["full"]["complex"][k] = measure_router(
                "sanic_router_full", run_stmt, args.total_iter
            )

    # ----------------------------------------------------------------------- #
    if not args.skip_xrtr:

        xrtr_router_minimal = create_xrtr_router(minimal_uris)

        for i, k in enumerate(num_vars):

            print_type_of_test(
                "MINIMAL, {} VARIABLE, SIMPLE STRING, NO-REPEAT".format(k)
            )
            run_stmt = gen_stmt(
                "xrtr_router_minimal.get",
                "minimal_uris",
                i,
                False,
                is_xrtr=True,
            )
            res["xrtr"]["min"]["simple"][k] = measure_router(
                "xrtr_router_minimal", run_stmt, args.total_iter
            )

            print_type_of_test(
                "MINIMAL, {} VARIABLE, COMPLEX STRING, NO-REPEAT".format(k)
            )
            run_stmt = gen_stmt(
                "xrtr_router_minimal.get",
                "minimal_uris",
                i,
                True,
                is_xrtr=True,
            )
            res["xrtr"]["min"]["complex"][k] = measure_router(
                "xrtr_router_minimal", run_stmt, args.total_iter
            )

        # ------------------------------------------------------------------- #
        xrtr_router_full = create_xrtr_router(lots_of_uris)

        for i, k in enumerate(num_vars):

            print_type_of_test(
                "FULL, {} VARIABLE, SIMPLE STRING, NO-REPEAT".format(k)
            )
            run_stmt = gen_stmt(
                "xrtr_router_full.get", "lots_of_uris", i, False, is_xrtr=True
            )
            res["xrtr"]["full"]["simple"][k] = measure_router(
                "xrtr_router_full", run_stmt, args.total_iter
            )

            print_type_of_test(
                "FULL, {} VARIABLE, COMPLEX STRING, NO-REPEAT".format(k)
            )
            run_stmt = gen_stmt(
                "xrtr_router_full.get", "lots_of_uris", i, True, is_xrtr=True
            )
            res["xrtr"]["full"]["complex"][k] = measure_router(
                "xrtr_router_full", run_stmt, args.total_iter
            )

    # ----------------------------------------------------------------------- #
    # skip helper

    def should_skip(frwk):
        if frwk == "falcon" and args.skip_falcon:
            return True
        elif frwk == "kua" and args.skip_kua:
            return True
        elif frwk == "routes" and args.skip_routes:
            return True
        elif frwk == "sanic" and args.skip_sanic:
            return True
        elif frwk == "xrtr" and args.skip_xrtr:
            return True
        return False

    # ----------------------------------------------------------------------- #
    # compact result

    print("\n\n-------------------------------------")
    print("COMPACT RESULT")
    print("-------------------------------------\n")
    for k in res:
        if should_skip(k):
            continue

        print(">> {}".format(k))
        print(
            "  - zero var, min routes: {:.6f} (~{:.2f} iter/sec)".format(
                *res[k]["min"]["simple"]["ZERO"]
            )
        )
        print(
            "  - 1 simple var, min routes: {:.6f} (~{:.2f} iter/sec)".format(
                *res[k]["min"]["simple"]["ONE"]
            )
        )
        print(
            "  - 2 simple var, min routes: {:.6f} (~{:.2f} iter/sec)".format(
                *res[k]["min"]["simple"]["TWO"]
            )
        )
        print(
            "  - 3 simple var, min routes: {:.6f} (~{:.2f} iter/sec)".format(
                *res[k]["min"]["simple"]["THREE"]
            )
        )
        print("")
        print(
            "  - zero var, min routes: {:.6f} (~{:.2f} iter/sec)".format(
                *res[k]["min"]["complex"]["ZERO"]
            )
        )
        print(
            "  - 1 complex var, min routes: {:.6f} (~{:.2f} iter/sec)".format(
                *res[k]["min"]["complex"]["ONE"]
            )
        )
        print(
            "  - 2 complex var, min routes: {:.6f} (~{:.2f} iter/sec)".format(
                *res[k]["min"]["complex"]["TWO"]
            )
        )
        print(
            "  - 3 complex var, min routes: {:.6f} (~{:.2f} iter/sec)".format(
                *res[k]["min"]["complex"]["THREE"]
            )
        )
        print("")
        print(
            "  - zero var, full routes: {:.6f} (~{:.2f} iter/sec)".format(
                *res[k]["full"]["simple"]["ZERO"]
            )
        )
        print(
            "  - 1 simple var, full routes: {:.6f} (~{:.2f} iter/sec)".format(
                *res[k]["full"]["simple"]["ONE"]
            )
        )
        print(
            "  - 2 simple var, full routes: {:.6f} (~{:.2f} iter/sec)".format(
                *res[k]["full"]["simple"]["TWO"]
            )
        )
        print(
            "  - 3 simple var, full routes: {:.6f} (~{:.2f} iter/sec)".format(
                *res[k]["full"]["simple"]["THREE"]
            )
        )
        print("")
        print(
            "  - zero var, full routes: {:.6f} (~{:.2f} iter/sec)".format(
                *res[k]["full"]["complex"]["ZERO"]
            )
        )
        print(
            "  - 1 complex var, full routes: {:.6f} (~{:.2f} iter/sec)".format(
                *res[k]["full"]["complex"]["ONE"]
            )
        )
        print(
            "  - 2 complex var, full routes: {:.6f} (~{:.2f} iter/sec)".format(
                *res[k]["full"]["complex"]["TWO"]
            )
        )
        print(
            "  - 3 complex var, full routes: {:.6f} (~{:.2f} iter/sec)".format(
                *res[k]["full"]["complex"]["THREE"]
            )
        )
        print("")

    if args.plot:
        frwks = res.keys()
        type_test = ["min", "full"]
        var_complexity = ["simple", "complex"]
        for tt in type_test:
            for vc in var_complexity:
                fig, ax = plt.subplots()
                for f in frwks:
                    if should_skip(f):
                        continue

                    series = [res[f][tt][vc][n][0] for n in num_vars]
                    ax.plot(series, label=f, marker="o")
                    for a, b in enumerate(series):
                        ax.text(a, b + 0.007, "{:.3f}s".format(b))
                ax.xaxis.set_major_formatter(plt.FuncFormatter(format_func))
                plt.title(
                    "{} routes, {} variables, {:,} iterations".format(
                        tt, vc, args.total_iter
                    )
                )
                plt.legend(loc="upper left")
                plt.ylabel("Time (in seconds)")
                plt.xlabel("Number of variables")

        plt.show()


def format_func(value, tick_number):  # NOTE this is ugly, I KNOW :-D
    if int(value) == value:
        return "{}".format(int(value))
    return ""


if __name__ == "__main__":
    main()
