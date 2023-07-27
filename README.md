# ship's log
The original idea was born in an hackaton in 2020, this new version, ship's logs, is an 
improvement of the original [Diário de Bordo](https://github.com/lumafepe/hackathon20-21)

### Usage
Uses the current day as the default name to the subtopic where the output is going to be generated


Simpler call is done by only providing the parent folder, in this case we'll be generated a a new folder with 
the current day


only one diary per subtopic
```
$ shipslogs <parent_folder> 
```

```
$ shipslogs <parent_folder> <sub_topic>
```

### Config

config.json


### Options
* -h, help

* -t <pathInput> <pathOutput>, from a given input path to a folder of images, "transcripts" the images to a new diary in the
output path

### Outputs
FIXME


--- 


Here is an example in how you to run.
In this example I'm starting a diary to the *myapp* folder, when is not provided a name for the subtopic the current
day will be the final name
```
$ shipslogs myapp 
```

Using this instance a name is provided to be the subtopic, in this case "example" id going to be the suptopic created
```
$ shipslogs myapp example
```


