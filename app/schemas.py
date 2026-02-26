#!/usr/bin/env python
# coding: utf-8

from pydantic import BaseModel


class PredictionRequest(BaseModel):
    credit_info_xml: str


class PredictionResponse(BaseModel):
    predicted_destruction_events: float

