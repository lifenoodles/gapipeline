About
==========
Gapipeline is a modular GA library written in python. It makes it trivial to compose customisable algorithn pipelines out of smaller discrete steps.

An algorithm is constructed as Pipeline of steps that all operate on shared data (the Message).
Pipelines can either be once off or repeating.
A discrete step in an pipeline is called a Task.
See the tasks folder for examples of some standard tasks you might find in an EA.
Tasks can also be categorised into Initialisers, Finalisers and Controllers.
In a standard pipeline, the message is passed into the pipeline and is processed by each task in order.
In a repeating pipeline, all initialisers are run once.
The rest of the tasks are then run continously, until the Controller task returns a False signal, at which point the finalisers are run once.
Pipelines can be composed programmatically but for best results you should use the YAML based pipeline builder.
A YAML specification is read and the required number of pipelines are created, this number depends on the amount of parameter permutations you have supplied in the specification.
See the pipelines folder for examples of pipeline specifications with multiple parameters.
The program in runner.py is used to actually construct and run the pipelines from a named file.
The examples given include pipelines that log to terminal and pipelines that collate results and store them on a remote server running a mongodb instance.
