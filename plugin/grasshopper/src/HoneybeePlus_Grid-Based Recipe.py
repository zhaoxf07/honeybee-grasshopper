# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Honeybee.
#
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Grid-based Recipe.

-

    Args:
        _sky: A radiance sky. Find honeybee skies under 02::Daylight::Light Sources.
        _analysisGrids: A list of analysis grids.
        _analysisType_: Analysis type. [0] illuminance(lux), [1] radiation (kwh),
            [2] luminance (Candela).
        _radiancePar_: Radiance parameters for Grid-based analysis. Find Radiance
            parameters node under 03::Daylight::Recipes.
    Returns:
        readMe!: Reports, errors, warnings, etc.
        analysisRecipe: Grid-based analysis recipe. Connect this recipe to
            Run Radiance Analysis to run a grid-based analysis.
"""

ghenv.Component.Name = "HoneybeePlus_Grid-Based Recipe"
ghenv.Component.NickName = 'gridBasedRecipe'
ghenv.Component.Message = 'VER 0.0.04\nFEB_07_2018'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '03 :: Daylight :: Recipe'
ghenv.Component.AdditionalHelpFromDocStrings = "2"

#import honeybee
#reload(honeybee.radiance.recipe.pointintime.gridbased)
try:
    from honeybee.radiance.recipe.pointintime.gridbased import GridBased
except ImportError as e:
    raise ImportError('\nFailed to import honeybee:\n\t{}'.format(e))


if _sky and _analysisGrids:
    
    # set a sunlight hours analysis recipe together if there are points
    analysisRecipe = GridBased(_sky, _analysisGrids, _analysisType_,
                               _radiancePar_)