#!/usr/bin/env python3 
import os
import platform
import glob


def get_driver_path(driver):
    supported = ["Darwin", "Linux"]
    op = platform.platform().split("-")
    if "x86_64" not in op:
        os.error("32-bit is not supported at the moment")

    if op[0] in supported:
        relative_path = "../drivers/{}/{}".format(op[0], driver)
    return relative_path


if __name__ == "__main__":
    print(get_driver_path("geckodriver"))

