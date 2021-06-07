import rosnode
import re

def topic_info(node_name):
    """
    ノードのpublish, subscribeを辞書で出力

    Parameters
    ----------
    node_name : 
        ノード名

    Returns
    -------
    {ノード名:[[publish1, publish2, ...], [subscribe1, subscribe2, ...]]} : dict
        
    """
    node_info = rosnode.get_node_info_description(node_name)
    split = re.split('Publications:|Subscriptions: |Services:', node_info)
    publish_list = re.findall(r'(?<=\* )[^\*]*\]', split[1])
    subscribe_list = re.findall(r'(?<=\* )[^\*]*\]', split[2])
    return {node_name:[publish_list, subscribe_list]}

def make_topic_info_list():
    """
    辞書型の各ノード情報をリストにしてまとめて出力

    Parameters
    ----------

    Returns
    -------
    [{ノード1:[[publish1, publish2, ...], [subscribe1, subscribe2, ...]]},
     {ノード2:[[publish1, publish2, ...], [subscribe1, subscribe2, ...]]},
     {ノード3:[[publish1, publish2, ...], [subscribe1, subscribe2, ...]]},
     , ...] : list
        
    """
    topic_info_list = []
    node_list = rosnode.get_node_names()
    for node in node_list:
        topic_info_list.append(topic_info(node))
    return topic_info_list


if __name__ == '__main__':
    print(make_topic_info_list())
