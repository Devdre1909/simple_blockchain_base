from crypt import methods
from urllib import response

from pytest import console_main
from blockchain import Blockchain

# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 17:30:29 2022

@author: devtemitope
"""
from blockchain import Blockchain
from flask import Flask, jsonify, request

app = Flask(__name__)

blc = Blockchain()

@app.route('/mine-block', methods=['GET'])
def mine_block():
  previous_block = blc.get_previous_block()
  previous_proof = previous_block['proof']
  previous_hash = blc.hash(previous_block)

  proof = blc.proof_of_work(previous_proof)

  block = blc.create_block(proof, previous_hash)

  response = {
    'message': 'Congratulations, you just mined a block!',
    'block': block
  }

  return jsonify(response), 200

@app.route('/get-chain', methods=['GET'])
def get_chain():
  response = {
    'chain': blc.chain,
    'length': len(blc.chain)
  }
  return jsonify(response), 200

@app.route('/check-chain', methods=['GET'])
def is_valid():
  valid_chain = blc.is_chain_valid(blc.chain)
  if valid_chain:
    response = {
      'message': 'Chain is all good '
    }
  else:
    response = {
      'message': 'Ops! You have been hacked'
    }

  return jsonify(response), 200

app.run(host='0.0.0.0', port=5000)