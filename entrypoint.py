import json

from ArubaCloud.PyArubaAPI import CloudInterface
from ArubaCloud.base.Errors import RequestFailed
from ArubaCloud.objects import SmartVmCreator
from pprint import pprint
import click

AVAILABLE_DATACENTERS = {
    1: 'DC1: Italy',
    2: 'DC2: Italy',
    3: 'DC3: Chech Republic',
    4: 'DC4: France',
    5: 'DC5: Germany',
    6: 'DC6: UK',
}


@click.group()
@click.option('-u', '--username', required=True)
@click.option('-p', '--password', required=True)
@click.option('-v', '--debug', is_flag=True, help=u'Show all performed operations')
@click.option('-d', '--datacenter', required=True, type=click.Choice(map(str, AVAILABLE_DATACENTERS.keys())),
              help='\n'.join(AVAILABLE_DATACENTERS.values()))
def cli(**kwargs):
    pass


@cli.command()
@click.option('-n', '--name', help=u'Show only templates with provided string in description')
@click.pass_context
def show_templates(ctx, **kwargs):
    ci = login_to_ci(**ctx.parent.params)
    print u"Getting list of hypervisors..."
    ci.get_hypervisors()
    pprint(ci.find_template(hv=4, **kwargs))


@cli.command()
@click.option('--admin-password', required=True, help=u'Admin password for root user to connect by ssh')
@click.option('-t', '--template-id', required=True, type=int,
              help=u'Server template ID. Run "show_templates" to see all options')
@click.option('-s', '--size', required=True, type=click.Choice(['small', 'medium', 'large', 'extralarge']))
@click.argument('names', nargs=-1, required=True)
@click.pass_context
def create_server(ctx, names, size, **kwargs):
    ci = login_to_ci(**ctx.parent.params)
    debug = ctx.parent.params['debug']

    for name in names:
        c = SmartVmCreator(auth_obj=ci.auth, name=name, **kwargs)
        c.set_type(size=size)
        print u"Creating SmartVm {}...".format(name)
        if debug:
            print u"DEBUG: request data"
            pprint(json.loads(c.get_json()))
        if not c.commit(url=ci.wcf_baseurl, debug=debug):
            print u"Error while creating server, aborting."
            break
        print u"Server successfully created\n"


def login_to_ci(username, password, datacenter, **kwargs):
    try:
        print u"Logging to ArubaCloud DC{}".format(datacenter)
        ci = CloudInterface(dc=int(datacenter))
        ci.login(username=username, password=password, load=False)
        return ci
    except RequestFailed as e:
        raise click.ClickException(u'Error while trying to connect to ArubaCloud. More info: \n{}'.format(e))


if __name__ == '__main__':
    cli()
