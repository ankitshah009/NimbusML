# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------------------------
# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
Resizer
"""

__all__ = ["Resizer"]


from sklearn.base import TransformerMixin

from ...base_transform import BaseTransform
from ...internal.core.feature_extraction.image._resizer import Resizer as core
from ...internal.utils.utils import trace


class Resizer(core, BaseTransform, TransformerMixin):
    """

    Resizes an image to a specified dimension using a specified
    resizing method.

    .. remarks::
        ``Resizer`` resizes an image to the specified height and width
        using a specified resizing method. The input variables to this
        transforms must
        be images, typically the result of the ``Loader`` transform.

    :param columns: A dictionary of key-value pairs, where key is the output
        column name and value is the input column name.

        * Multiple key-value pairs are allowed.
        * Input column type: :ref:`Picture`.
        * Output column type: :ref:`Picture`.
        * If the output column names are same as the input column names, then
        simply specify ``columns`` as a list of strings.

        The << operator can be used to set this value (see
        `Column Operator </nimbusml/concepts/columns>`_)

        For example
         * Resizer(columns={'out1':'input1', 'out2':'input2'})
         * Resizer() << {'out1':'input1', 'out2':'input2'}

        For more details see `Columns </nimbusml/concepts/columns>`_.

    :param image_width: Specifies the width of the scaled image in pixels.
        The default value is 224.

    :param image_height: Specifies the height of the scaled image in pixels.
        The default value is 224.

    :param resizing: Specified the resizing method to use. Note that all
        methods
        are using bilinear interpolation. The options are:

        * ``"IsoPad"``: The image is resizerd such that the aspect ratio is
        preserved.
          If needed, the image is padded with black to fit the new width or
        height.
        * ``"IsoCrop"``: The image is resizerd such that the aspect ratio is
        preserved.
          If needed, the image is cropped to fit the new width or height.
        * ``"Aniso"``: The image is stretched to the new width and height,
        without
          preserving the aspect ratio.

        The default value is ``"IsoCrop"``.

    :param crop_anchor: Anchor for cropping.

    :param params: Additional arguments sent to compute engine.

    .. seealso::
        :py:class:`Loader <nimbusml.feature_extraction.image.Loader>`,
        :py:class:`PixelExtractor
        <nimbusml.feature_extraction.image.PixelExtractor>`.

    .. index:: transform, image

    Example:
       .. literalinclude:: /../nimbusml/examples/Image.py
              :language: python
    """

    @trace
    def __init__(
            self,
            image_width=0,
            image_height=0,
            resizing='IsoCrop',
            crop_anchor='Center',
            columns=None,
            **params):

        if columns:
            params['columns'] = columns
        BaseTransform.__init__(self, **params)
        core.__init__(
            self,
            image_width=image_width,
            image_height=image_height,
            resizing=resizing,
            crop_anchor=crop_anchor,
            **params)
        self._columns = columns

    def get_params(self, deep=False):
        """
        Get the parameters for this operator.
        """
        return core.get_params(self)
