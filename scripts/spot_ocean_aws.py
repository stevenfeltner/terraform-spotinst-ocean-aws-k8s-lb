import click
import json
import requests
import os


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
@click.option('--debug', default=False, type=bool)
@click.pass_context
def add(debug, *args, **kwargs):
    """Add a LoadBalancer to existing Ocean Cluster"""

    loadbalancerarn = str(kwargs.get('loadbalancerarn'))
    cluster_id = str(kwargs.get('clusterid'))
    account_id = str(kwargs.get('accountid'))
    token = str(kwargs.get('token'))

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + token
    }
    url = 'https://api.spotinst.io/ocean/aws/k8s/cluster/' + cluster_id + '?accountId=' + account_id

    try:
        r = requests.get(url, headers=headers)
        data = json.loads(r.text)
        if r.status_code != 200:
            print('Status ', r.status_code)
            print(data)
        else:
            loadbalancers = []
            items = data['response']['items']
            for x in items:
                loadbalancers = x['compute']['launchSpecification']['loadBalancers']
            if debug:
                print("Ocean LoadBalancer List: ", loadbalancers)
            loadbalancers.append({'arn': loadbalancerarn, 'type': 'TARGET_GROUP'})
            if debug:
                print("New appended Ocean LoadBalancer List: " ,loadbalancers)
            headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + token
            }
            url = 'https://api.spotinst.io/ocean/aws/k8s/cluster/' + cluster_id + '?accountId=' + account_id
            data = {"cluster": {"compute": {"launchSpecification": {"loadBalancers": loadbalancers}}}}

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
    except Exception as e:
        print(e)


@cli.command()
@click.argument('loadbalancerarn', )
@click.argument('clusterid', )
@click.argument('accountid', )
@click.argument('token', )
@click.option('--debug', default=False, type=bool)
@click.pass_context
def delete(debug, *args, **kwargs):
    """Delete a LoadBalancer from existing Ocean Cluster"""
    loadbalancerarn = str(kwargs.get('loadbalancerarn'))
    cluster_id = str(kwargs.get('clusterid'))
    account_id = str(kwargs.get('accountid'))
    token = str(kwargs.get('token'))

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + token
    }
    url = 'https://api.spotinst.io/ocean/aws/k8s/cluster/' + cluster_id + '?accountId=' + account_id

    try:
        r = requests.get(url, headers=headers)
        data = json.loads(r.text)
        if r.status_code != 200:
            print('Status ', r.status_code)
            print(data)
        else:
            loadbalancers = []
            items = data['response']['items']
            for x in items:
                loadbalancers = x['compute']['launchSpecification']['loadBalancers']
            if debug:
                print("Ocean LoadBalancer List: ", loadbalancers)

            newloadbalancers = []
            for x in loadbalancers:
                if x['arn'] == loadbalancerarn:
                    pass
                else:
                    newloadbalancers.append(x)
            if debug:
                print("New LoadBalancer List: ", newloadbalancers)
            headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + token
            }
            url = 'https://api.spotinst.io/ocean/aws/k8s/cluster/' + cluster_id + '?accountId=' + account_id
            data = {"cluster": {"compute": {"launchSpecification": {"loadBalancers": newloadbalancers}}}}

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
    except Exception as e:
        print(e)


if __name__ == "__main__":
    cli()
