from cli import main
import misc

if __name__ == "__main__":
    if not misc.read_config()["installed"]:
        misc.run_install()
    main()