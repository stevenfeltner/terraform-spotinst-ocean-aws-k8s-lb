import click
import json
import requests
import os

#from spotinst_sdk2 import SpotinstSession


@click.group()
@click.pass_context
def cli(ctx, *args, **kwargs):
    ctx.obj = {}
    #session = SpotinstSession()
    #ctx.obj['client'] = session.client("ocean_aws")


@cli.command()
@click.argument('loadbalancerarn', )
@click.argument('clusterid', )
@click.argument('accountid', )
@click.argument('token', )
@click.pass_context
def add(ctx, *args, **kwargs):
    """Add a LoadBalancer to existing Ocean Cluster"""

    loadBalancerarn = str(kwargs.get('loadbalancerarn'))
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
            items = data['response']['items']
            for x in items:
                loadBalancers = x['compute']['launchSpecification']['loadBalancers']
            #print(loadBalancers)
            loadBalancers.append({'arn': loadBalancerarn, 'type': 'TARGET_GROUP'})
            #print(loadBalancers)
            headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + token
            }
            url = 'https://api.spotinst.io/ocean/aws/k8s/cluster/' + cluster_id + '?accountId=' + account_id
            data = {"cluster":{"compute":{"launchSpecification":{"loadBalancers":loadBalancers}}}}

            try:
                r = requests.put(url, headers=headers, json=data)
                data = json.loads(r.text)
                if r.status_code != 200:
                    print('Status ', r.status_code)
                    print(data)
                else:
                    print('Status ', r.status_code)
            except Exception as e:
                print(e)
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
    loadBalancerarn = str(kwargs.get('loadbalancerarn'))
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
            items = data['response']['items']
            for x in items:
                loadBalancers = x['compute']['launchSpecification']['loadBalancers']
            #print(loadBalancers)

            newloadBalancers = []
            for x in loadBalancers:
                if x['arn'] == loadBalancerarn:
                    pass
                else:
                    newloadBalancers.append(x)
            #print(newloadBalancers)
            headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + token
            }
            url = 'https://api.spotinst.io/ocean/aws/k8s/cluster/' + cluster_id + '?accountId=' + account_id
            data = {"cluster":{"compute":{"launchSpecification":{"loadBalancers":newloadBalancers}}}}

            try:
                r = requests.put(url, headers=headers, json=data)
                data = json.loads(r.text)
                if r.status_code != 200:
                    print('Status ', r.status_code)
                    print(data)
                else:
                    print('Status ', r.status_code)
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    cli()
