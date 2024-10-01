# Conformal Map Plot

Visualise complex functions with `matplotlib` with a conformal plot - the preimage is plotted in the $xy$ plane and the image in the $uv$ plane.

## Info about Files

`conformal_map.py` plots a specified grid (vertical + horizontal lines) and then the image.

`plot_circles.py` allows you to specify a circle, and then plot the image of that circle.

`plot_line.py` allows you to specify a line, and then plot the image of that line.

## How to Use

Clone the repo. Then, edit the desired file with your line/circle of interest and the function you want to apply (see file comments for info). Note that you must use `numpy` syntax. Anything that would need to be edited is at the very top of each file.

Then, you can run
```
./start.sh [l|c|m]
```
where `l` execute `plot_line.py`, `c` executes `plot_circles.py`, and `m` executes `conformal_map.py`. 

Alternatively, you can just execute the desired script with
```
python3 [name_of_file]
```

