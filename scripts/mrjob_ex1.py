#!/usr/bin/env
"""
    This example was adapted from the mrjob documentation:
    
    https://pythonhosted.org/mrjob/guides/quickstart.html
"""

from mrjob.job import MRJob

class MRWordFrequencyCount(MRJob):
    
    def mapper(self, _, line):
        ## remove whitespace from front and end of line
        line = line.strip()
        ## yield the length of the line (including spaces)
        yield "chars", len(line)
        # yield the number of words on the line
        yield "words", len(line.split())
        # yield the number of lines (always 1)
        yield "lines", 1
    
    def reducer(self, key, values):
        ## the reducer simply sums all the "chars", "words" and "lines" values
        yield key, sum(values)


if __name__ == '__main__':
    MRWordFrequencyCount.run()
