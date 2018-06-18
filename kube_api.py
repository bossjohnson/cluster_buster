from kubernetes import client, config

def get_pods(namespace='default'):
    # Configs can be set in Configuration class directly or using helper utility
    config.load_kube_config()

    v1 = client.CoreV1Api()
    print("Listing pods with their IPs in namespace {}:".format(namespace))
    ret = v1.list_pod_for_all_namespaces(watch=False)

    pods = []

    for i in ret.items:
        if i.metadata.namespace == namespace:
            print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
            pods.append(i)

    return pods
