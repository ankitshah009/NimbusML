# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------------------------
# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
WordEmbedding
"""

__all__ = ["WordEmbedding"]


from ....entrypoints.transforms_wordembeddings import transforms_wordembeddings
from ....utils.utils import trace
from ...base_pipeline_item import BasePipelineItem, DefaultSignature


class WordEmbedding(BasePipelineItem, DefaultSignature):
    """

    Word Embeddings transform is a text featurizer which converts vectors
    of text tokens into sentence vectors using a pre-trained model.

    .. remarks::
        WordEmbeddings wrap different embedding models, such as
        Sentiment Specific Word Embedding(SSWE). Users can specify
        which embedding to use. The
        available options are various versions of `GloVe Models
        <https://nlp.stanford.edu/projects/glove/>`_, `FastText
        <https://en.wikipedia.org/wiki/FastText>`_, and `Sswe
        <http://anthology.aclweb.org/P/P14/P14-1146.pdf>`_.


    :param model_kind: Pre-trained model used to create the vocabulary.
        Available options are: 'GloVe50D', 'GloVe100D', 'GloVe200D',
        'GloVe300D', 'GloVeTwitter25D', 'GloVeTwitter50D',
        'GloVeTwitter100D', 'GloVeTwitter200D', 'FastTextWikipedia300D',
        'SentimentSpecificWordEmbedding'.

    :param custom_lookup_table: Filename for custom word embedding model.

    :param params: Additional arguments sent to compute engine.

    .. note::

        As ``WordEmbedding`` requires a column with text vector, e.g.
        <'This', 'is', 'good'>, users need to create an input column by:

        * concatenating columns with TX type,
        * or using the ``output_tokens_column_name`` for ``NGramFeaturizer()`` to
        convert a column with sentences like "This is good" into <'This',
        'is', 'good'>.


        In the following example, after the ``NGramFeaturizer``, features
        named *ngram.__* are generated.
        A new column named *ngram_TransformedText* is also created with the
        text vector, similar as running ``.split(' ')``.
        However, due to the variable length of this column it cannot be
        properly converted to pandas dataframe,
        thus any pipelines/transforms output this text vector column will
        throw errors. However, we use *ngram_TransformedText* as the input to
        ``WordEmbedding``, the
        *ngram_TransformedText* column will be overwritten by the output from
        ``WordEmbedding``. The output from ``WordEmbedding`` is named
        *ngram_TransformedText.__*

    .. seealso::
        :py:class:`NGramFeaturizer
        <nimbusml.feature_extraction.text.NGramFeaturizer>`,
        :py:class:`Sentiment
        <nimbusml.feature_extraction.text.Sentiment>`.

    .. index:: dnn, features, embedding

    Example:
       .. literalinclude:: /../nimbusml/examples/WordEmbedding.py
              :language: python
    """

    @trace
    def __init__(
            self,
            model_kind='SentimentSpecificWordEmbedding',
            custom_lookup_table=None,
            **params):
        BasePipelineItem.__init__(
            self, type='transform', **params)

        self.model_kind = model_kind
        self.custom_lookup_table = custom_lookup_table

    @property
    def _entrypoint(self):
        return transforms_wordembeddings

    @trace
    def _get_node(self, **all_args):

        input_columns = self.input
        if input_columns is None and 'input' in all_args:
            input_columns = all_args['input']
        if 'input' in all_args:
            all_args.pop('input')

        output_columns = self.output
        if output_columns is None and 'output' in all_args:
            output_columns = all_args['output']
        if 'output' in all_args:
            all_args.pop('output')

        # validate input
        if input_columns is None:
            raise ValueError(
                "'None' input passed when it cannot be none.")

        if not isinstance(input_columns, list):
            raise ValueError(
                "input has to be a list of strings, instead got %s" %
                type(input_columns))

        # validate output
        if output_columns is None:
            output_columns = input_columns

        if not isinstance(output_columns, list):
            raise ValueError(
                "output has to be a list of strings, instead got %s" %
                type(output_columns))

        algo_args = dict(
            column=[
                dict(
                    Source=i,
                    Name=o) for i,
                o in zip(
                    input_columns,
                    output_columns)] if input_columns else None,
            model_kind=self.model_kind,
            custom_lookup_table=self.custom_lookup_table)

        all_args.update(algo_args)
        return self._entrypoint(**all_args)
