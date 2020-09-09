# -*- coding: utf-8 -*-
import click
import logging


@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
@click.argument('output_filepath', type=click.Path())
def run(input_filepath, output_filepath):
    """
    Runs data processing scripts to turn raw data from (../data/raw) into
    cleaned data ready to be analyzed (saved in ../data/processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('Making final data set from raw data...')


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    run()
