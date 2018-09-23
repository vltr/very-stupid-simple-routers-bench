import random
import sys
import timeit
import uuid

import kua
import matplotlib.pyplot as plt
from extras import Endpoint, res_factory
from falcon.routing import CompiledRouter
from routes import Mapper
from sanic.router import Router
from uridata import BenchData, ParamFormat, SimpleData
from xrtr import RadixTree

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


def measure_router(router_name, run_stmt, times=100000):
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
    falcon_compiled_router_minimal = create_falcon_router(minimal_uris)

    for i, k in enumerate(num_vars):

        print_type_of_test(
            "MINIMAL, {} VARIABLE, SIMPLE STRING, NO-REPEAT".format(k)
        )
        run_stmt = gen_stmt(
            "falcon_compiled_router_minimal.find", "minimal_uris", i, False
        )
        res["falcon"]["min"]["simple"][k] = measure_router(
            "falcon_compiled_router_minimal", run_stmt
        )

        print_type_of_test(
            "MINIMAL, {} VARIABLE, COMPLEX STRING, NO-REPEAT".format(k)
        )
        run_stmt = gen_stmt(
            "falcon_compiled_router_minimal.find", "minimal_uris", i, True
        )
        res["falcon"]["min"]["complex"][k] = measure_router(
            "falcon_compiled_router_minimal", run_stmt
        )

    # ----------------------------------------------------------------------- #
    falcon_compiled_router_full = create_falcon_router(lots_of_uris)

    for i, k in enumerate(num_vars):

        print_type_of_test(
            "FULL, {} VARIABLE, SIMPLE STRING, NO-REPEAT".format(k)
        )
        run_stmt = gen_stmt(
            "falcon_compiled_router_full.find", "lots_of_uris", i, False
        )
        res["falcon"]["full"]["simple"][k] = measure_router(
            "falcon_compiled_router_full", run_stmt
        )

        print_type_of_test(
            "FULL, {} VARIABLE, COMPLEX STRING, NO-REPEAT".format(k)
        )
        run_stmt = gen_stmt(
            "falcon_compiled_router_full.find", "lots_of_uris", i, True
        )
        res["falcon"]["full"]["complex"][k] = measure_router(
            "falcon_compiled_router_full", run_stmt
        )

    # ----------------------------------------------------------------------- #
    kua_router_minimal = create_kua_router(minimal_uris)

    for i, k in enumerate(num_vars):

        print_type_of_test(
            "MINIMAL, {} VARIABLE, SIMPLE STRING, NO-REPEAT".format(k)
        )
        run_stmt = gen_stmt(
            "kua_router_minimal.match", "minimal_uris", i, False
        )
        res["kua"]["min"]["simple"][k] = measure_router(
            "kua_router_minimal", run_stmt
        )

        print_type_of_test(
            "MINIMAL, {} VARIABLE, COMPLEX STRING, NO-REPEAT".format(k)
        )
        run_stmt = gen_stmt(
            "kua_router_minimal.match", "minimal_uris", i, True
        )
        res["kua"]["min"]["complex"][k] = measure_router(
            "kua_router_minimal", run_stmt
        )

    # ----------------------------------------------------------------------- #
    kua_router_full = create_kua_router(lots_of_uris)

    for i, k in enumerate(num_vars):

        print_type_of_test(
            "FULL, {} VARIABLE, SIMPLE STRING, NO-REPEAT".format(k)
        )
        run_stmt = gen_stmt(
            "kua_router_full.match", "lots_of_uris", i, False
        )
        res["kua"]["full"]["simple"][k] = measure_router(
            "kua_router_full", run_stmt
        )

        print_type_of_test(
            "FULL, {} VARIABLE, COMPLEX STRING, NO-REPEAT".format(k)
        )
        run_stmt = gen_stmt(
            "kua_router_full.match", "lots_of_uris", i, True
        )
        res["kua"]["full"]["complex"][k] = measure_router(
            "kua_router_full", run_stmt
        )

    # ----------------------------------------------------------------------- #
    routes_router_minimal = create_routes_router(minimal_uris)

    for i, k in enumerate(num_vars):

        print_type_of_test(
            "MINIMAL, {} VARIABLE, SIMPLE STRING, NO-REPEAT".format(k)
        )
        run_stmt = gen_stmt(
            "routes_router_minimal.match", "minimal_uris", i, False
        )
        res["routes"]["min"]["simple"][k] = measure_router(
            "routes_router_minimal", run_stmt
        )

        print_type_of_test(
            "MINIMAL, {} VARIABLE, COMPLEX STRING, NO-REPEAT".format(k)
        )
        run_stmt = gen_stmt(
            "routes_router_minimal.match", "minimal_uris", i, True
        )
        res["routes"]["min"]["complex"][k] = measure_router(
            "routes_router_minimal", run_stmt
        )

    # ----------------------------------------------------------------------- #
    routes_router_full = create_routes_router(lots_of_uris)

    for i, k in enumerate(num_vars):

        print_type_of_test(
            "FULL, {} VARIABLE, SIMPLE STRING, NO-REPEAT".format(k)
        )
        run_stmt = gen_stmt(
            "routes_router_full.match", "lots_of_uris", i, False
        )
        res["routes"]["full"]["simple"][k] = measure_router(
            "routes_router_full", run_stmt
        )

        print_type_of_test(
            "FULL, {} VARIABLE, COMPLEX STRING, NO-REPEAT".format(k)
        )
        run_stmt = gen_stmt(
            "routes_router_full.match", "lots_of_uris", i, True
        )
        res["routes"]["full"]["complex"][k] = measure_router(
            "routes_router_full", run_stmt
        )

    # ----------------------------------------------------------------------- #
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
            "sanic_router_minimal", run_stmt
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
            "sanic_router_minimal", run_stmt
        )

    # ----------------------------------------------------------------------- #
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
            "sanic_router_full", run_stmt
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
            "sanic_router_full", run_stmt
        )

    # ----------------------------------------------------------------------- #
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
            "xrtr_router_minimal", run_stmt
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
            "xrtr_router_minimal", run_stmt
        )

    # ----------------------------------------------------------------------- #
    xrtr_router_full = create_xrtr_router(lots_of_uris)

    for i, k in enumerate(num_vars):

        print_type_of_test(
            "FULL, {} VARIABLE, SIMPLE STRING, NO-REPEAT".format(k)
        )
        run_stmt = gen_stmt(
            "xrtr_router_full.get", "lots_of_uris", i, False, is_xrtr=True
        )
        res["xrtr"]["full"]["simple"][k] = measure_router(
            "xrtr_router_full", run_stmt
        )

        print_type_of_test(
            "FULL, {} VARIABLE, COMPLEX STRING, NO-REPEAT".format(k)
        )
        run_stmt = gen_stmt(
            "xrtr_router_full.get", "lots_of_uris", i, True, is_xrtr=True
        )
        res["xrtr"]["full"]["complex"][k] = measure_router(
            "xrtr_router_full", run_stmt
        )

    # ----------------------------------------------------------------------- #
    # compact result

    print("\n\n-------------------------------------")
    print("COMPACT RESULT")
    print("-------------------------------------\n")
    for k in res:
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

    if "plot" in sys.argv:
        i = 1
        frwks = res.keys()
        type_test = ["min", "full"]
        var_complexity = ["simple", "complex"]
        for tt in type_test:
            for vc in var_complexity:
                plt.figure(i)
                i += 1
                for f in frwks:
                    series = [res[f][tt][vc][n][0] for n in num_vars]
                    plt.plot(series, label=f, marker="o")
                plt.title("{} routes, {} variables".format(tt, vc))
                plt.legend(loc='lower right')
                plt.ylabel('Time')
                plt.xlabel('Variables')
        plt.show()


if __name__ == "__main__":
    main()
