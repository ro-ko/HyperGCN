'''
data: coauthorship/cocitation
dataset: cora/dblp/acm for coauthorship and cora/citeseer/pubmed for cocitation
'''
data = "coauthorship" #실험 종류
dataset = "dblp" #실험 데이터 출처



'''
mediators: Laplacian with mediators (True) or Laplacian without mediators (False)
fast: FastHyperGCN (True) or not fast (False)
split: train-test split used for the dataset
'''
mediators = False #1-Hyper or HyperGCN
fast = False #FastHyperGCN
split = 1



'''
gpu: gpu number to use
cuda: True or False
seed: an integer
'''
gpu = 3
cuda = True
seed = 5



'''
model related parameters
depth: number of hidden layers in the graph convolutional network (GCN)
dropout: dropout probability for GCN hidden layer
epochs: number of training epochs
'''
depth = 2
dropout = 0.5
epochs = 200




'''
parameters for optimisation
rate: learning rate
decay: weight decay
'''
rate = 0.01
decay = 0.0005

'''
model for hypergraph neral network
'''
model="HyperGCN"

import configargparse, os,sys,inspect
from configargparse import YAMLConfigFileParser



def parse():
	"""
	adds and parses arguments / hyperparameters
	"""
	default = os.path.join(current(), data + ".yml")
	p = configargparse.ArgParser(config_file_parser_class = YAMLConfigFileParser, default_config_files=[default])
	p.add('-c', '--my-config', is_config_file=True, help='config file path')
	p.add('--data', type=str, default=data, help='data name (coauthorship/cocitation)')
	p.add('--dataset', type=str, default=dataset, help='dataset name (e.g.: cora/dblp/acm for coauthorship, cora/citeseer/pubmed for cocitation)')
	p.add('--mediators', type=bool, default=mediators, help='True for Laplacian with mediators, False for Laplacian without mediators')
	p.add('--fast', type=bool, default=fast, help='faster version of HyperGCN (True)')
	p.add('--split', type=int, default=split, help='train-test split used for the dataset')
	p.add('--depth', type=int, default=depth, help='number of hidden layers')
	p.add('--dropout', type=float, default=dropout, help='dropout probability for GCN hidden layer')
	p.add('--rate', type=float, default=rate, help='learning rate')
	p.add('--decay', type=float, default=decay, help='weight decay')
	p.add('--epochs', type=int, default=epochs, help='number of epochs to train')
	p.add('--gpu', type=int, default=gpu, help='gpu number to use')
	p.add('--cuda', type=bool, default=cuda, help='cuda for gpu')
	p.add('--seed', type=int, default=seed, help='seed for randomness')
	p.add('-f') # for jupyter default
	p.add('--model', type=str, default=model, help='model for Hypergraph neural network')
	return p.parse_args()



def current():
	"""
	returns the current directory path
	"""
	current = os.path.abspath(inspect.getfile(inspect.currentframe()))
	head, tail = os.path.split(current)
	return head
