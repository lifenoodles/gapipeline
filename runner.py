import pypline
import argparse
import os

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="GA Pipeline Runner")
    parser.add_argument("-v", action="store_const", const=True,
        help="Verbose mode")
    parser.add_argument("filename")
    args = parser.parse_args()
    print dir(args)
    filename = args.filename
    filetype = os.path.splitext(filename)[1]
    if filetype == ".yaml":
        print "Parsing YAML"
        builder = pypline.YamlManagerBuilder()
        manager = builder.build_manager(filename)
        manager.generate_pipelines()
        print "Generated %i pipeline%s" % (len(manager.pipelines),
            "s" if len(manager.pipelines) > 1 else "")
        manager.execute(verbose=args.v)

    print "Run Complete"
