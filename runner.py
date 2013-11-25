import pypline
import argparse
import os

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="GA Pipeline Runner")
    parser.add_argument("filename")
    args = parser.parse_args()
    filename = args.filename
    filetype = os.path.splitext(filename)[1]
    print filetype
    if filetype == ".yaml":
        builder = pypline.YamlManagerBuilder()
        manager = builder.build_manager(filename)
        manager.generate_pipelines()
        manager.execute()

    print "Run Complete"
