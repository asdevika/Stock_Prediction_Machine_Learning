# -*- coding: utf-8 -*-
"""
Created on Mon May  6 03:27:34 2019

@author: Devika
"""

import argparse
import backtest
from backtest import TestStrategy
from feedforward_strat import FeedforwardStrategy
import feedforward_nn
import data_process as dp
import graph


def arg_parser():
    parser = argparse.ArgumentParser(description="Stock prediction model", formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-b', '--btest', help='Run backtest with the model',
            default=None, choices=['test', 'feedforward', 'recurrent', 'cnn'])
    parser.add_argument('-t', '--train', help='Train a model', default=None,
            choices=['feedforward', 'recurrent', 'cnn'])
    parser.add_argument('-g', '--graph', help='Graph', nargs='*', choices=['test', 'feedforward', 'recurrent', 'cnn'])

    args = parser.parse_args()
    print("In arg_parser:%s" % args)
    return args


class InputHandler:
    def __init__(self, inputs):
        print ("Args =%s" % inputs)
        self.inputs = inputs
        if self.inputs.train:
            self.train(self.inputs.train)
        if self.inputs.btest:
            if self.inputs.btest == "test":
                self.run(TestStrategy)
            elif self.inputs.btest == "feedforward":
                self.run(FeedforwardStrategy)
        if self.inputs.graph:
            if len(self.inputs.graph) != 0:
                graph(self.inputs.graph)
            else:
                print("Taking feed")
                graph(['feedforward', 'recurrent', 'cnn'])

    @staticmethod
    def run(strategy):
        backtest_obj = backtest.Backtest(stock_symbol='XOM', strategy=strategy)
        backtest_obj.run(plot=True)

    @staticmethod
    def train(model):
        inputs = dp.create_data()
        if model == "feedforward":
            feedforward_nn.feedforward_neural_network(inputs)
        elif model == "recurrent":
            rnn_lstm.recurrent_neural_network(inputs)
        elif model == 'cnn':
            conv.conv_neural_network(inputs)