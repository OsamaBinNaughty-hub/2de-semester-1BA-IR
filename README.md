# Analyse2-1BA

Current building status ![CI](https://github.com/OsamaBinNaughty-hub/2de-semester-1BA-IR/workflows/CI/badge.svg?branch=master)

[Go to builds](https://github.com/OsamaBinNaughty-hub/2de-semester-1BA-IR/actions)


## Building on Windows with docker

```
Eenmalig in te voeren
> docker build -t samclercky/latexsamenvatting .
Vanaf dan enkel dit commando (PowerShell) met pwd hoofdmap project
> docker run --rm -v $(pwd):/source samclercky/latexsamenvatting build.py <NAAM VAN MAP>
```
