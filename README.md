# Containers #

A small application that finds the most efficient container selection for a given collection of container sizes and load.

## Requirements ##

* Python 3.6.1

## Usage ##

`$ make run`

## Example ##

```
containers: 2, 3, 5
load: 6
> 3, 3
load: 9
> 5, 2, 2
load: 11
> 5, 3, 3
```

## Testing ##

`$ make test`
