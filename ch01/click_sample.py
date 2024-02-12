import click

@click.command()
@click.option('--message', default='Hello', help='Message to echo.')
def echo(message):
    print(message)

if __name__ == '__main__':
    echo()
