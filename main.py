import argparse
import sys
import shlex


def parse_arguments(cli_args=None):
    """Returns argparse object with attributes for each CLI arg.

    Args:
        cli_args: A list of strings representing CLI args to use.

    Returns:
        A argparse instance.
    """

    arg_parse = argparse.ArgumentParser(
        prog="Devogen CLI",
        description="Generates GitHub Actions YML files based on a project.",
    )
    arg_parse.add_argument(
        dest="lang",
        type=str,
        nargs="+",
        default=[],
    )

    cli_args_str = f"python3 -m {__package__} "
    if cli_args is not None:
        cli_args_str += " ".join(cli_args)
    else:
        cli_args_str += " ".join([shlex.quote(x) for x in sys.argv[1:]])

    return arg_parse.parse_args(cli_args)


def main(cli_args=None):
    """Main function.

    Args:
        cli_args: A list of strings representing CLI args to use.
    """
    print("Devogen CLI")
    args = parse_arguments(cli_args)
    print(args)
    return 0


if __name__ == "__main__":
    main()
