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
$ python bench.py --plot
```

And some nice graphics will show you some results :wink:

### Full list of options

To get the full list of options (such as skip one or more router or change the number os iterations), see the help message:

```
$ python bench.py --help
```


## Results

All tests ran under Python 3.7.0 with 100k iterations (1mi iterations seems like an eternity for certain routers, changed it at will using the `--iters N` argument if you **really** want to).

### Arch Linux, Kernel 4.18.9-1-ck-piledriver, AMD FX-8320E @ 3.5GHz / DDR3 @ 2133MHz

```
-------------------------------------
COMPACT RESULT
-------------------------------------

>> falcon
  - zero var, min routes: 0.234772 (~425945.77 iter/sec)
  - 1 simple var, min routes: 0.716286 (~139609.00 iter/sec)
  - 2 simple var, min routes: 1.053934 (~94882.62 iter/sec)
  - 3 simple var, min routes: 1.344903 (~74354.82 iter/sec)

  - zero var, min routes: 0.230354 (~434114.73 iter/sec)
  - 1 complex var, min routes: 1.202745 (~83143.16 iter/sec)
  - 2 complex var, min routes: 2.002099 (~49947.59 iter/sec)
  - 3 complex var, min routes: 2.800711 (~35705.22 iter/sec)

  - zero var, full routes: 0.298365 (~335159.98 iter/sec)
  - 1 simple var, full routes: 0.881712 (~113415.68 iter/sec)
  - 2 simple var, full routes: 1.252508 (~79839.84 iter/sec)
  - 3 simple var, full routes: 1.436183 (~69628.99 iter/sec)

  - zero var, full routes: 0.304111 (~328827.42 iter/sec)
  - 1 complex var, full routes: 1.385500 (~72176.12 iter/sec)
  - 2 complex var, full routes: 2.241384 (~44615.28 iter/sec)
  - 3 complex var, full routes: 2.932565 (~34099.84 iter/sec)

>> kua
  - zero var, min routes: 0.995842 (~100417.56 iter/sec)
  - 1 simple var, min routes: 1.567503 (~63795.74 iter/sec)
  - 2 simple var, min routes: 2.021110 (~49477.75 iter/sec)
  - 3 simple var, min routes: 2.450809 (~40802.86 iter/sec)

  - zero var, min routes: 1.002442 (~99756.42 iter/sec)
  - 1 complex var, min routes: 2.190235 (~45657.21 iter/sec)
  - 2 complex var, min routes: 3.073963 (~32531.30 iter/sec)
  - 3 complex var, min routes: 4.307481 (~23215.43 iter/sec)

  - zero var, full routes: 0.888096 (~112600.45 iter/sec)
  - 1 simple var, full routes: 1.878441 (~53235.64 iter/sec)
  - 2 simple var, full routes: 2.370091 (~42192.48 iter/sec)
  - 3 simple var, full routes: 2.610198 (~38311.28 iter/sec)

  - zero var, full routes: 0.891885 (~112122.06 iter/sec)
  - 1 complex var, full routes: 2.734446 (~36570.48 iter/sec)
  - 2 complex var, full routes: 3.417224 (~29263.52 iter/sec)
  - 3 complex var, full routes: 4.127116 (~24229.99 iter/sec)

>> routes
  - zero var, min routes: 1.124339 (~88941.16 iter/sec)
  - 1 simple var, min routes: 2.079985 (~48077.28 iter/sec)
  - 2 simple var, min routes: 2.697940 (~37065.32 iter/sec)
  - 3 simple var, min routes: 3.265924 (~30619.20 iter/sec)

  - zero var, min routes: 1.118118 (~89436.00 iter/sec)
  - 1 complex var, min routes: 2.846352 (~35132.69 iter/sec)
  - 2 complex var, min routes: 4.093908 (~24426.54 iter/sec)
  - 3 complex var, min routes: 5.334730 (~18745.09 iter/sec)

  - zero var, full routes: 54.874229 (~1822.35 iter/sec)
  - 1 simple var, full routes: 59.564871 (~1678.84 iter/sec)
  - 2 simple var, full routes: 59.553458 (~1679.16 iter/sec)
  - 3 simple var, full routes: 57.535719 (~1738.05 iter/sec)

  - zero var, full routes: 56.162940 (~1780.53 iter/sec)
  - 1 complex var, full routes: 59.397681 (~1683.57 iter/sec)
  - 2 complex var, full routes: 59.642849 (~1676.65 iter/sec)
  - 3 complex var, full routes: 60.488186 (~1653.22 iter/sec)

>> sanic
  - zero var, min routes: 0.045980 (~2174861.76 iter/sec)
  - 1 simple var, min routes: 1.870525 (~53460.94 iter/sec)
  - 2 simple var, min routes: 2.355239 (~42458.54 iter/sec)
  - 3 simple var, min routes: 2.819531 (~35466.89 iter/sec)

  - zero var, min routes: 0.047931 (~2086340.58 iter/sec)
  - 1 complex var, min routes: 2.442416 (~40943.06 iter/sec)
  - 2 complex var, min routes: 3.557304 (~28111.18 iter/sec)
  - 3 complex var, min routes: 4.601165 (~21733.63 iter/sec)

  - zero var, full routes: 0.060204 (~1661019.97 iter/sec)
  - 1 simple var, full routes: 1.831989 (~54585.49 iter/sec)
  - 2 simple var, full routes: 2.363051 (~42318.17 iter/sec)
  - 3 simple var, full routes: 2.760774 (~36221.72 iter/sec)

  - zero var, full routes: 0.055037 (~1816967.59 iter/sec)
  - 1 complex var, full routes: 2.468317 (~40513.43 iter/sec)
  - 2 complex var, full routes: 3.488036 (~28669.43 iter/sec)
  - 3 complex var, full routes: 4.403709 (~22708.13 iter/sec)

>> xrtr
  - zero var, min routes: 0.083421 (~1198742.26 iter/sec)
  - 1 simple var, min routes: 0.590754 (~169275.06 iter/sec)
  - 2 simple var, min routes: 0.895412 (~111680.49 iter/sec)
  - 3 simple var, min routes: 1.194680 (~83704.41 iter/sec)

  - zero var, min routes: 0.083700 (~1194746.91 iter/sec)
  - 1 complex var, min routes: 1.079695 (~92618.75 iter/sec)
  - 2 complex var, min routes: 1.855863 (~53883.30 iter/sec)
  - 3 complex var, min routes: 2.647138 (~37776.65 iter/sec)

  - zero var, full routes: 0.116233 (~860340.84 iter/sec)
  - 1 simple var, full routes: 0.706042 (~141634.61 iter/sec)
  - 2 simple var, full routes: 0.999158 (~100084.24 iter/sec)
  - 3 simple var, full routes: 1.238376 (~80750.90 iter/sec)

  - zero var, full routes: 0.113627 (~880069.78 iter/sec)
  - 1 complex var, full routes: 1.188098 (~84168.16 iter/sec)
  - 2 complex var, full routes: 1.947556 (~51346.39 iter/sec)
  - 3 complex var, full routes: 2.630886 (~38010.00 iter/sec)
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
