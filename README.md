# Python Blockchain

Simple Blockchain built with python.

Blockchain - An immutable, sequential chain of records called blocks that contain transactions, files, or any data you would like. (chained together by hashes)

Hash function - A function that takes in an input value, and creates an output value deterministic of the input value. For any x input value, you will always receive the same y output value whenever the hash function is ran. Usually displayed as a hexadecimal number and are generally irreversible (one-way - can't figure out the input if you only know the output).

Proof of Work Algorithm (PoW) - How new blocks are created or mined on the blockchain. The goal of PoW is to discover a number which solves a problem. The number must be difficult to find but easy to verify (computationally speaking) by anyone on the network.

Note to self: We've got a basic blockchain that accepts transactions and allows us to mine new blocks. But the whole point of blockchains is that they should be decentralized. And if they're decentralized we need to ensure that they all reflect the same chain. This is called the problem of Consensus, and we'll have to implement a Consensus Algorithm if we want more than one node in our network. Resolve this by making a rule that the longest valid chain is authoritative - is the defacto. 

Requirements:
Pip
Python 3.6+
Flask == 0.12.2
requests == 2.18.4
HTTP Client: Postman, cURL, etc.

To Do:
Set up Blockchain as an API with Flask