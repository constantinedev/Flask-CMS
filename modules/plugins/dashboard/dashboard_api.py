import re, io, os, sys, ast, json, sqlite_utils, logging, pgpy
from flask import Flask, Blueprint, request, make_response, Response, jsonify, redirect, url_for, render_template, flash, abort

def page_loader():
  if request.method == "GET":
    return render_template('plugins/dashboard/dash00.htm', pag="dsahboard", title="Dashboard")