# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
Transforms.CategoricalOneHotVectorizer
"""

import numbers

from ..utils.entrypoints import EntryPoint
from ..utils.utils import try_set, unlist


def transforms_categoricalonehotvectorizer(
        column,
        data,
        output_data=None,
        model=None,
        max_num_terms=1000000,
        output_kind='Indicator',
        term=None,
        sort='ByOccurrence',
        text_key_values=True,
        **params):
    """
    **Description**
        Converts the categorical value into an indicator array by building a
        dictionary of categories based on the data and using the id
        in the dictionary as the index in the array.

    :param column: New column definition(s) (optional form: name:src)
        (inputs).
    :param data: Input dataset (inputs).
    :param max_num_terms: Maximum number of keys to keep per column
        when auto-training (inputs).
    :param output_kind: Output kind: Bag (multi-set vector), Ind
        (indicator vector), or Key (index) (inputs).
    :param term: List of terms (inputs).
    :param sort: How items should be ordered when vectorized. By
        default, they will be in the order encountered. If by value
        items are sorted according to their default comparison, for
        example, text sorting will be case sensitive (for example,
        'A' then 'Z' then 'a'). (inputs).
    :param text_key_values: Whether key value metadata should be
        text, regardless of the actual input type (inputs).
    :param output_data: Transformed dataset (outputs).
    :param model: Transform model (outputs).
    """

    entrypoint_name = 'Transforms.CategoricalOneHotVectorizer'
    inputs = {}
    outputs = {}

    if column is not None:
        inputs['Column'] = try_set(
            obj=column,
            none_acceptable=False,
            is_of_type=list,
            is_column=True)
    if data is not None:
        inputs['Data'] = try_set(
            obj=data,
            none_acceptable=False,
            is_of_type=str)
    if max_num_terms is not None:
        inputs['MaxNumTerms'] = try_set(
            obj=max_num_terms,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if output_kind is not None:
        inputs['OutputKind'] = try_set(
            obj=output_kind,
            none_acceptable=True,
            is_of_type=str,
            values=[
                'Bag',
                'Indicator',
                'Key',
                'Binary'])
    if term is not None:
        inputs['Term'] = try_set(
            obj=term,
            none_acceptable=True,
            is_of_type=list)
    if sort is not None:
        inputs['Sort'] = try_set(
            obj=sort,
            none_acceptable=True,
            is_of_type=str,
            values=[
                'ByOccurrence',
                'ByValue'])
    if text_key_values is not None:
        inputs['TextKeyValues'] = try_set(
            obj=text_key_values,
            none_acceptable=True,
            is_of_type=bool)
    if output_data is not None:
        outputs['OutputData'] = try_set(
            obj=output_data,
            none_acceptable=False,
            is_of_type=str)
    if model is not None:
        outputs['Model'] = try_set(
            obj=model,
            none_acceptable=False,
            is_of_type=str)

    input_variables = {
        x for x in unlist(inputs.values())
        if isinstance(x, str) and x.startswith("$")}
    output_variables = {
        x for x in unlist(outputs.values())
        if isinstance(x, str) and x.startswith("$")}

    entrypoint = EntryPoint(
        name=entrypoint_name, inputs=inputs, outputs=outputs,
        input_variables=input_variables,
        output_variables=output_variables)
    return entrypoint
