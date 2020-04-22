# Daily Wiki

Featured articles are considered to be some of the best articles Wikipedia has to offer, as determined by Wikipedia's editors. Daily Wiki is an application that scans the [featured articles](https://en.wikipedia.org/wiki/Wikipedia:Featured_articles) and chooses one article per category. Then the selected articles are exported to a file where the user can read, following the porvided link.\

## Requirements

- python >= 3.7
- pip3.7

## Installation

To install the application run:

```bash
pip3.7 install .
```

## Usage

To run the application and extract the files:

```bash
daily_wki
```

## Data export

The data are exported in json format in the file `/tmp/wiki-{data}.json`
