# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
Predefined
"""


from ..utils.entrypoints import Component


def predefined(
        **params):
    """
    **Description**
        Remover with predefined list of stop words.

    """

    entrypoint_name = 'Predefined'
    settings = {}

    component = Component(
        name=entrypoint_name,
        settings=settings,
        kind='StopWordsRemover')
    return component
