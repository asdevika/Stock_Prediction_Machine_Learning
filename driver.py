# -*- coding: utf-8 -*-
"""
Created on Mon May  6 00:30:56 2019

@author: Devika
"""

from arg_handler import arg_parser, InputHandler
    

def main():
    inputs = arg_parser()
    InputHandler(inputs)


if __name__ == "__main__":
    main()