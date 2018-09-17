# A very stupid and simple python routers benchmark script

This repository contains a script to benchmark how certain Python routers takes to find a URL based on number of variables (one, two or three), if this variable is "simple" ("1234", "5555") or "complex" (an UUID, like "33e587fa-a4dd-425a-abdc-14de5d5c3175") and the number of total routes created inside each router (3 for the minimum test, ~400 for the full test).

The tests were created to minimize the impact of caching mechanisms (if any) in the final results.

The compared routers are:

- [Falcon](https://falcon.readthedocs.io/en/stable/);
- [kua](https://github.com/nitely/kua);
- [Routes](https://routes.readthedocs.io/en/latest/);
- [Sanic](https://github.com/huge-success/sanic);
- [xrtr](https://github.com/vltr/xrtr);

**ATTENTION**: if there's anything wrong with the method used to compare between all these routers, please let me know.

## IMPORTANT NOTE

This is by no means a source of "choice" between Python URL routing solutions. It just seeks speed and has no error testing whatsoever. It is purelly informative in a very simple way.

## How to run

First, make sure you have Python 3.5+ on your machine. Then, install all the requirements:

```
$ pip install -r requirements.txt
```

Then, simply call Python to execute the `bench.py` file:

```
$ python bench.py
```

And wait.

## Results

The results in my workstation machine (an old AMD octacore machine) showed this (compact result) in 100k iterations (1mi iterations seems like an eternity for certain routers, changed it at will):

```
-------------------------------------
COMPACT RESULT
-------------------------------------

>> falcon
  - 1 simple var, min routes: 0.704239 (~141997.24 iter/sec)
  - 2 simple var, min routes: 1.027677 (~97306.79 iter/sec)
  - 3 simple var, min routes: 1.341360 (~74551.19 iter/sec)

  - 1 complex var, min routes: 1.185571 (~84347.51 iter/sec)
  - 2 complex var, min routes: 1.968017 (~50812.56 iter/sec)
  - 3 complex var, min routes: 2.776771 (~36013.06 iter/sec)

  - 1 simple var, full routes: 0.850326 (~117601.94 iter/sec)
  - 2 simple var, full routes: 1.155972 (~86507.32 iter/sec)
  - 3 simple var, full routes: 1.456818 (~68642.77 iter/sec)

  - 1 complex var, full routes: 1.338926 (~74686.72 iter/sec)
  - 2 complex var, full routes: 2.092623 (~47786.91 iter/sec)
  - 3 complex var, full routes: 2.875468 (~34776.95 iter/sec)

>> kua
  - 1 simple var, min routes: 1.591491 (~62834.15 iter/sec)
  - 2 simple var, min routes: 2.024441 (~49396.36 iter/sec)
  - 3 simple var, min routes: 2.463072 (~40599.71 iter/sec)

  - 1 complex var, min routes: 2.145458 (~46610.11 iter/sec)
  - 2 complex var, min routes: 3.071196 (~32560.60 iter/sec)
  - 3 complex var, min routes: 3.983415 (~25104.09 iter/sec)

  - 1 simple var, full routes: 1.802163 (~55488.89 iter/sec)
  - 2 simple var, full routes: 2.285745 (~43749.42 iter/sec)
  - 3 simple var, full routes: 2.834983 (~35273.57 iter/sec)

  - 1 complex var, full routes: 2.342263 (~42693.76 iter/sec)
  - 2 complex var, full routes: 3.312664 (~30187.19 iter/sec)
  - 3 complex var, full routes: 4.478111 (~22330.85 iter/sec)

>> routes
  - 1 simple var, min routes: 1.963598 (~50926.91 iter/sec)
  - 2 simple var, min routes: 2.690208 (~37171.85 iter/sec)
  - 3 simple var, min routes: 3.142183 (~31825.01 iter/sec)

  - 1 complex var, min routes: 2.699040 (~37050.21 iter/sec)
  - 2 complex var, min routes: 3.957306 (~25269.72 iter/sec)
  - 3 complex var, min routes: 5.075390 (~19702.92 iter/sec)

  - 1 simple var, full routes: 65.826421 (~1519.15 iter/sec)
  - 2 simple var, full routes: 66.532962 (~1503.01 iter/sec)
  - 3 simple var, full routes: 66.543111 (~1502.79 iter/sec)

  - 1 complex var, full routes: 67.104753 (~1490.21 iter/sec)
  - 2 complex var, full routes: 67.662397 (~1477.93 iter/sec)
  - 3 complex var, full routes: 68.831951 (~1452.81 iter/sec)

>> sanic
  - 1 simple var, min routes: 1.620019 (~61727.65 iter/sec)
  - 2 simple var, min routes: 2.238985 (~44663.10 iter/sec)
  - 3 simple var, min routes: 2.675230 (~37379.96 iter/sec)

  - 1 complex var, min routes: 2.330683 (~42905.88 iter/sec)
  - 2 complex var, min routes: 3.317751 (~30140.90 iter/sec)
  - 3 complex var, min routes: 4.287243 (~23325.01 iter/sec)

  - 1 simple var, full routes: 1.658040 (~60312.18 iter/sec)
  - 2 simple var, full routes: 2.291906 (~43631.81 iter/sec)
  - 3 simple var, full routes: 2.755308 (~36293.59 iter/sec)

  - 1 complex var, full routes: 2.370231 (~42189.98 iter/sec)
  - 2 complex var, full routes: 3.423689 (~29208.26 iter/sec)
  - 3 complex var, full routes: 4.343138 (~23024.83 iter/sec)

>> xrtr
  - 1 simple var, min routes: 0.537971 (~185883.66 iter/sec)
  - 2 simple var, min routes: 0.869508 (~115007.51 iter/sec)
  - 3 simple var, min routes: 1.166801 (~85704.40 iter/sec)

  - 1 complex var, min routes: 1.020490 (~97992.14 iter/sec)
  - 2 complex var, min routes: 1.773249 (~56393.67 iter/sec)
  - 3 complex var, min routes: 2.541739 (~39343.14 iter/sec)

  - 1 simple var, full routes: 0.631841 (~158267.67 iter/sec)
  - 2 simple var, full routes: 0.925295 (~108073.70 iter/sec)
  - 3 simple var, full routes: 1.242445 (~80486.43 iter/sec)

  - 1 complex var, full routes: 1.098753 (~91012.23 iter/sec)
  - 2 complex var, full routes: 1.854167 (~53932.58 iter/sec)
  - 3 complex var, full routes: 2.639418 (~37887.13 iter/sec)
```

## Thanks

For [this repository](https://github.com/richardolsson/falcon-routing-survey) from one of the Falcon project contributors that inspired me to do this benchmark script.

## License

**No license**. Make sure to know what this means.
