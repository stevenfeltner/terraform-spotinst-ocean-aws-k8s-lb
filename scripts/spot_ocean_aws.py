import click
import json
import requests
import time


# from spotinst_sdk2 import SpotinstSession


@click.group()
@click.pass_context
def cli(ctx, *args, **kwargs):
    ctx.obj = {}
    # session = SpotinstSession()
    # ctx.obj['client'] = session.client("ocean_aws")


@cli.command()
@click.argument('loadbalancerarn', )
@click.argument('clusterid', )
@click.argument('accountid', )
@click.argument('token', )
@click.pass_context
def add(ctx, *args, **kwargs):
    """Add a LoadBalancer to existing Ocean Cluster"""

    loadbalancerarn = str(kwargs.get('loadbalancerarn'))
    cluster_id = str(kwargs.get('clusterid'))
    account_id = str(kwargs.get('accountid'))
    token = str(kwargs.get('token'))
    # debug = True

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + token
    }
    url = 'https://api.spotinst.io/ocean/aws/k8s/cluster/' + cluster_id + '/loadBalancer/attach?accountId=' + account_id
    data = {"loadBalancers": [{"arn": loadbalancerarn}]}
    try:
        r = requests.put(url, headers=headers, json=data)
        data = json.loads(r.text)
        if r.status_code != 200:
            print('Status: ', r.status_code, ' Failed to add LoadBalancer')
            print(data)
        else:
            print('Status: ', r.status_code, ' Successfully added LoadBalancer to Ocean cluster')
    except Exception as e:
        print(e)


@cli.command()
@click.argument('loadbalancerarn', )
@click.argument('clusterid', )
@click.argument('accountid', )
@click.argument('token', )
@click.pass_context
def delete(ctx, *args, **kwargs):
    """Delete a LoadBalancer from existing Ocean Cluster"""

    loadbalancerarn = str(kwargs.get('loadbalancerarn'))
    cluster_id = str(kwargs.get('clusterid'))
    account_id = str(kwargs.get('accountid'))
    token = str(kwargs.get('token'))

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + token
    }
    url = 'https://api.spotinst.io/ocean/aws/k8s/cluster/' + cluster_id + '/loadBalancer/detach?accountId=' + account_id
    data = {"loadBalancers": [{"arn":loadbalancerarn}]}

    try:
        r = requests.put(url, headers=headers, json=data)
        data = json.loads(r.text)
        if r.status_code != 200:
            print('Status ', r.status_code, ' Failed to remove LoadBalancer')
            print(data)
        else:
            print('Status ', r.status_code, ' Successfully removed LoadBalancer from Ocean cluster')
    except Exception as e:
        print(e)


if __name__ == "__main__":
    cli()
