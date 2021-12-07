def super_func() -> None:
    print(1)
    print(1)


def main() -> None:
    print(2)
    super_func()


if __name__ == '__main__':
    main()
