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

### Running with matplotlib

Yes, visuals can help you better visualize the data gathered by this simple bench. In order to do that, install `matplotlib` (if not already from the `requirements.txt` file) and run:

```
$ python bench.py plot
```

And some nice graphics will show you some results :wink:

## Results

All tests ran under Python 3.7.0 with 100k iterations (1mi iterations seems like an eternity for certain routers, changed it at will [here](https://github.com/vltr/very-stupid-simple-routers-bench/blob/master/bench.py#L71) if you want to).

### Arch Linux, Kernel 4.18.6-1-ck-piledriver, AMD FX-8320 @ 3.5GHz / DDR3 @ 2133MHz

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

### Arch Linux, Kernel 4.18.9-1-ck-broadwell, Intel(R) Core(TM) i7-6800K CPU @ 3.40GHz / DDR4 @ 2400MHz

```
-------------------------------------
COMPACT RESULT
-------------------------------------

>> falcon
  - zero var, min routes: 0.119366 (~837759.55 iter/sec)
  - 1 simple var, min routes: 0.304096 (~328843.38 iter/sec)
  - 2 simple var, min routes: 0.468356 (~213512.82 iter/sec)
  - 3 simple var, min routes: 0.609251 (~164136.05 iter/sec)

  - zero var, min routes: 0.108997 (~917457.26 iter/sec)
  - 1 complex var, min routes: 0.544848 (~183537.59 iter/sec)
  - 2 complex var, min routes: 0.940255 (~106354.13 iter/sec)
  - 3 complex var, min routes: 1.278260 (~78231.37 iter/sec)

  - zero var, full routes: 0.139780 (~715411.14 iter/sec)
  - 1 simple var, full routes: 0.339929 (~294179.12 iter/sec)
  - 2 simple var, full routes: 0.531617 (~188105.27 iter/sec)
  - 3 simple var, full routes: 0.667763 (~149753.81 iter/sec)

  - zero var, full routes: 0.137087 (~729461.43 iter/sec)
  - 1 complex var, full routes: 0.570697 (~175224.27 iter/sec)
  - 2 complex var, full routes: 0.973429 (~102729.64 iter/sec)
  - 3 complex var, full routes: 1.381971 (~72360.41 iter/sec)

>> kua
  - zero var, min routes: 0.460693 (~217064.48 iter/sec)
  - 1 simple var, min routes: 0.678799 (~147318.98 iter/sec)
  - 2 simple var, min routes: 0.906734 (~110285.93 iter/sec)
  - 3 simple var, min routes: 1.146357 (~87232.87 iter/sec)

  - zero var, min routes: 0.447368 (~223529.43 iter/sec)
  - 1 complex var, min routes: 1.002988 (~99702.08 iter/sec)
  - 2 complex var, min routes: 1.374558 (~72750.65 iter/sec)
  - 3 complex var, min routes: 1.805264 (~55393.56 iter/sec)

  - zero var, full routes: 0.477919 (~209240.62 iter/sec)
  - 1 simple var, full routes: 0.703609 (~142124.45 iter/sec)
  - 2 simple var, full routes: 0.988402 (~101173.38 iter/sec)
  - 3 simple var, full routes: 1.163763 (~85928.18 iter/sec)

  - zero var, full routes: 0.480467 (~208130.94 iter/sec)
  - 1 complex var, full routes: 0.960929 (~104065.95 iter/sec)
  - 2 complex var, full routes: 1.524108 (~65612.14 iter/sec)
  - 3 complex var, full routes: 1.917865 (~52141.31 iter/sec)

>> routes
  - zero var, min routes: 0.446431 (~223998.57 iter/sec)
  - 1 simple var, min routes: 0.841726 (~118803.52 iter/sec)
  - 2 simple var, min routes: 1.115815 (~89620.63 iter/sec)
  - 3 simple var, min routes: 1.391164 (~71882.23 iter/sec)

  - zero var, min routes: 0.487309 (~205208.55 iter/sec)
  - 1 complex var, min routes: 1.280685 (~78083.19 iter/sec)
  - 2 complex var, min routes: 1.883202 (~53101.04 iter/sec)
  - 3 complex var, min routes: 2.458447 (~40676.08 iter/sec)

  - zero var, full routes: 18.161956 (~5506.01 iter/sec)
  - 1 simple var, full routes: 18.176620 (~5501.57 iter/sec)
  - 2 simple var, full routes: 18.668618 (~5356.58 iter/sec)
  - 3 simple var, full routes: 19.384975 (~5158.63 iter/sec)

  - zero var, full routes: 18.245845 (~5480.70 iter/sec)
  - 1 complex var, full routes: 19.008201 (~5260.89 iter/sec)
  - 2 complex var, full routes: 19.641993 (~5091.13 iter/sec)
  - 3 complex var, full routes: 20.054814 (~4986.33 iter/sec)

>> sanic
  - zero var, min routes: 0.026549 (~3766600.77 iter/sec)
  - 1 simple var, min routes: 0.657751 (~152033.18 iter/sec)
  - 2 simple var, min routes: 0.946884 (~105609.57 iter/sec)
  - 3 simple var, min routes: 1.162184 (~86044.87 iter/sec)

  - zero var, min routes: 0.026706 (~3744473.53 iter/sec)
  - 1 complex var, min routes: 1.084642 (~92196.31 iter/sec)
  - 2 complex var, min routes: 1.627452 (~61445.76 iter/sec)
  - 3 complex var, min routes: 2.014620 (~49637.16 iter/sec)

  - zero var, full routes: 0.026568 (~3763915.62 iter/sec)
  - 1 simple var, full routes: 0.668679 (~149548.63 iter/sec)
  - 2 simple var, full routes: 1.003672 (~99634.14 iter/sec)
  - 3 simple var, full routes: 1.179775 (~84761.94 iter/sec)

  - zero var, full routes: 0.026542 (~3767622.39 iter/sec)
  - 1 complex var, full routes: 1.045743 (~95625.83 iter/sec)
  - 2 complex var, full routes: 1.559313 (~64130.82 iter/sec)
  - 3 complex var, full routes: 2.076079 (~48167.72 iter/sec)

>> xrtr
  - zero var, min routes: 0.039170 (~2552996.11 iter/sec)
  - 1 simple var, min routes: 0.240454 (~415880.03 iter/sec)
  - 2 simple var, min routes: 0.414304 (~241368.62 iter/sec)
  - 3 simple var, min routes: 0.533694 (~187373.22 iter/sec)

  - zero var, min routes: 0.040754 (~2453721.82 iter/sec)
  - 1 complex var, min routes: 0.501171 (~199532.65 iter/sec)
  - 2 complex var, min routes: 0.869394 (~115022.67 iter/sec)
  - 3 complex var, min routes: 1.251118 (~79928.50 iter/sec)

  - zero var, full routes: 0.070174 (~1425027.45 iter/sec)
  - 1 simple var, full routes: 0.243520 (~410644.24 iter/sec)
  - 2 simple var, full routes: 0.445411 (~224511.59 iter/sec)
  - 3 simple var, full routes: 0.550372 (~181695.38 iter/sec)

  - zero var, full routes: 0.069872 (~1431192.66 iter/sec)
  - 1 complex var, full routes: 0.492423 (~203077.64 iter/sec)
  - 2 complex var, full routes: 0.906885 (~110267.52 iter/sec)
  - 3 complex var, full routes: 1.250664 (~79957.55 iter/sec)
```

## Thanks

For [this repository](https://github.com/richardolsson/falcon-routing-survey) from one of the Falcon project contributors that inspired me to do this benchmark script.

## License

**No license**. Make sure to know what this means.
