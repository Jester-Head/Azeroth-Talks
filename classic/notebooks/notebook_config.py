# Custom color palettes for thematic visualizations

# General forum themes
import re
from matplotlib import pyplot as plt
import seaborn as sns


FORUM_COLORS = {
    'Season of Discovery': '#F2CB05',                      # Golden Yellow
    'WoW Classic General Discussion': '#D95323',           # Burnt Orange
    'WoW Classic Bug Report': '#8C241B',                   # Dark Red
    'WoW Classic Hardcore': '#E42028',                     # Bright Red
    'Wrath of the Lich King Classic Discussion': '#2397d1ff'  # Vivid Blue
}

# Wrath of the Lich King expansion theme colors
WOTLK_COLORS = {
    'uranian_blue': '#A8D2F0',
    'light_turquoise': '#56BFBF',
    'bright_light_turquoise': '#55D9CC',
    'light_sky_blue': '#60C2D7',
    'bright_turquoise': '#4ED9D9',
    'cyan_teal': '#3AA8BF',
    'medium_cyan': '#2D90A6',
    'prussian_blue': '#0A2842',
    'deep_cyan_blue': '#1C618C',
    'dark_cyan_blue': '#1F5B73',
    'dark_navy_blue': '#011826'
}


WOTLK_BAR_COLORS = {
    'bar_color': '#3AA8BF',
    'glow_color': '#4ED9D9',
    'background_color': '#0A2842'
}
# WoW Classic expansion theme colors
CLASSIC_COLORS = {
    'burnt_orange': '#DD6D1F',
    'muted_bronze': '#A8803D',
    'golden_yellow': '#F4AA17',
    'bright_yellow': '#FCD006',
    'deep_blue': '#004A81',
    'vibrant_yellow': '#FFFC01',
    'vivid_orange': '#FF4700',
    'bright_blue': '#0070FF',
    'wow_blue': '#001B3D',
    'wow_orange': '#D25400',
    'wow_yellow': '#F5F100'
}
# Logo specific colors
LOGO_COLORS = {
    'bar_color': '#FFFC01',
    'glow_color': '#FF4700',
    'background_color': '#0070FF'
}

# Class specific colors
CLASS_COLORS = {
    'Death Knight': '#C41F3B',  # Dark Red
    'Druid': '#FF7C0A',         # Deep Orange
    'Hunter': '#ABD473',        # Pale Green
    'Mage': '#3FC7EB',          # Bright Cyan
    'Paladin': '#F58CBA',       # Light Pink
    'Priest': '#FFFFFF',        # White
    'Rogue': '#FFF569',         # Light Yellow
    'Shaman': '#0070DD',        # Medium Blue
    'Warlock': '#8788EE',       # Light Purple
    'Warrior': '#C69B6D'        # Tan/Brown
}


# WoW colors indicating quality
ITEM_QUALITY_COLORS = {
    "Poor": "#9d9d9d",  # Gray
    "Common": "#ffffff",  # White
    "Uncommon": "#1eff00",  # Green
    "Rare": "#0070dd",  # Blue
    "Epic": "#a335ee",  # Purple
    "Legendary": "#ff8000",  # Orange
    "Artifact": "#e6cc80",  # Light Gold
    "Heirloom": "#00ccff",  # Blizzard Blue
}

ASHENVALE = {'Moonstone': '#7cabb6',
             'Russian Violet': '#200d44',
             'Moss Green': '#929a84',
             'Myrtle Green': '#4C7B86',
             'Indigo Dye': '#07435F',
             'Midnight Green': '#135867',
             'Prussian blue': '#06364C'}

HARDCORE_WOW = {'Silver': '#b9b0ae',
                'Davys Gray': '#4E5056',
                'Fire Truck': '#C42326',
                'Raisin Black': '#24272E'}


class CustomizePlot:
    """
    A class for customizing and creating thematic visualizations with predefined color schemes.
    """

    def __init__(self):
        """
        Initializes the CustomizePlot class.
        """
        pass

    def create_subplots(self, plt_items, titles, figsize=(20, 10)):
        """
        Creates subplots for a variable number of items (e.g., word clouds or images), each with a title.

        Parameters:
        - plt_items: List of matplotlib objects to display.
        - titles: List of titles for each subplot.
        - figsize: Optional tuple specifying figure size.
        """
        n = len(plt_items)
        fig, ax = plt.subplots(1, n, figsize=figsize)

        for i in range(n):
            try:
                ax[i].imshow(plt_items[i].to_image(), interpolation='bilinear')
                ax[i].set_title(titles[i])
            except Exception as e:
                ax[i].text(0.5, 0.5, 'Image Not Available',
                           ha='center', va='center')
                print(f"Error displaying image: {e}")
            ax[i].axis('off')

        plt.tight_layout()
        plt.show()

    def create_custom_barplots(self, data_list, x_col, y_col, titles, bar_colors, glow_colors, background_colors, font_color='white',
                               font_size=12, title_color='black', orientation='h'):
        """
        Creates custom bar plots for a variable number of datasets with specific aesthetic customizations.

        Parameters:
        - data_list: List of dataframes to plot.
        - x_col: The column name to plot on the x-axis.
        - y_col: The column name to plot on the y-axis.
        - titles: List of titles for each plot.
        - bar_colors: List of colors for the bars.
        - glow_colors: List of colors for the bar edges (glow effect).
        - background_colors: List of colors for the plot background.
        - font_color: Color of the font for text elements.
        - font_size: Size of the font for text elements.
        - title_color: Color of the plot titles.
        - orientation: Orientation of the bars ('h' for horizontal, 'v' for vertical).
        """
        n = len(data_list)

        fig, axes = plt.subplots(1, n, figsize=(20, 3*n))

        plt.gcf().set_facecolor(background_colors[0])
        for i, data in enumerate(data_list):
            ax = sns.barplot(x=x_col, y=y_col, data=data,
                             color=bar_colors[i], linewidth=2.5, edgecolor=glow_colors[i], ax=axes[i])

            ax.set_facecolor(background_colors[i])
            axes[i].set_facecolor(background_colors[i])
            axes[i].set_title(titles[i], color=title_color, fontsize=font_size)
            axes[i].set_xlabel(x_col.capitalize(),
                               fontsize=font_size, color=font_color)
            axes[i].set_ylabel(y_col.capitalize(),
                               fontsize=font_size, color=font_color)
            axes[i].tick_params(axis='x', rotation=40,
                                labelsize=font_size, colors=font_color)
            axes[i].tick_params(
                axis='y', labelsize=font_size, colors=font_color)
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.spines['left'].set_color(font_color)
            ax.spines['bottom'].set_color(font_color)

            for p in ax.patches:
                value = p.get_width() if orientation == 'h' else p.get_height()
                x_pos = p.get_x() + p.get_width() / 2 if orientation == 'h' else p.get_width()
                y_pos = p.get_y() + p.get_height() / 2 if orientation == 'h' else p.get_height()
                ha = 'center' if orientation == 'h' else 'left'
                va = 'center' if orientation == 'h' else 'bottom'
                xytext = (5, 0) if orientation == 'h' else (0, 5)

                ax.annotate(format(value, '.0f'), (x_pos, y_pos), ha=ha, va=va, xytext=xytext, textcoords='offset points', color=font_color,
                            fontsize=font_size)

        plt.tight_layout()
        plt.show()

    def plot_sentiment_subplots(self, dataframe, sentiments, colors, face_color, background_color, title_color, titles):
        """
        Plots sentiment data on separate subplots with customized aesthetics.

        Parameters:
        - dataframe: DataFrame containing sentiment data.
        - sentiments: List of sentiment categories (e.g., ['neg', 'neu', 'pos']).
        - colors: List of colors for each sentiment plot.
        - face_color: Color for the face of each subplot.
        - background_color: Color for the background of the figure.
        - title_color: Color for the titles and labels.
        - titles: List of titles for each subplot.
        """

        # Create a 3x1 subplot layout
        fig, axes = plt.subplots(len(sentiments), 1, figsize=(20, 15))

        # Plotting each sentiment on its subplot
        for i, sentiment in enumerate(sentiments):
            sns.lineplot(ax=axes[i], x=dataframe.index, y=dataframe[sentiment],
                         color=colors[i], marker='o', label=sentiment)
            axes[i].set_facecolor(face_color)
            axes[i].set_title(titles[i], fontsize=20, color=title_color)
            axes[i].set_xlabel('Date', fontsize=16, color=title_color)
            axes[i].tick_params(axis='x', colors=title_color)
            axes[i].tick_params(axis='y', colors=title_color)

        # Set the background color of the figure
        fig.patch.set_facecolor(background_color)

        # Common ylabel
        fig.text(0.04, 0.5, 'Mean Sentiment Score', va='center', rotation='vertical',
                 color=title_color, fontsize=14)

        plt.tight_layout(pad=6.0)
        plt.show()

    def plot_sentiment_category_counts(self, df, title, x_col, y_col, palette, face_color, background_color, edge_color, title_color,
                                       rotation=40,
                                       fontsize=(20, 14, 16)):
        """
        Plots a bar plot for sentiment category counts with customized styling.

        Parameters:
        - df: DataFrame containing the data to plot.
        - title: The plot title.
        - x_col: The name of the column to be used for the x-axis.
        - y_col: The name of the column to be used for the y-axis.
        - palette: Color palette for the bars.
        - face_color: Color for the face of the plot.
        - background_color: Color for the background of the figure.
        - edge_color: Color for the edge of the bars.
        - title_color: Color for the title and labels.
        - rotation: Degree of rotation for x-axis labels.
        - fontsize: A tuple (title_fontsize, label_fontsize, tick_fontsize) specifying the font sizes.
        """

        plt.figure(figsize=(10, 6))

        # Set the face and background colors
        plt.gca().set_facecolor(face_color)
        plt.gcf().set_facecolor(background_color)

        # Create the barplot
        sns.barplot(x=x_col, y=y_col, data=df, palette=palette,
                    linewidth=2, edgecolor=edge_color)

        # Title and labels with customizations
        plt.title(title, fontsize=fontsize[0], color=title_color)
        plt.xlabel(x_col, fontsize=fontsize[1], color=title_color)
        plt.ylabel(y_col, fontsize=fontsize[1], color=title_color)

        # Tick parameters
        plt.xticks(rotation=rotation, fontsize=fontsize[2], color=title_color)
        plt.yticks(fontsize=fontsize[2], color=title_color)

        plt.show()

    @staticmethod
    def hyphen_highlight(cell):
        """
        Highlights hyphenated words in a cell with HTML styling.

        Parameters:
        - cell: The cell content to be processed.

        Returns:
        - The processed cell content with hyphenated words highlighted.
        """
        hyphenated_highlight = r'\b\w+(?:-\w+)+\b'
        highlighted = re.sub(
            hyphenated_highlight, lambda x: f"<span style='color: red;'><strong>{x.group()}</strong></span>", cell)
        return highlighted

    @staticmethod
    def hyphen_slash_highlight(cell):
        """
        Highlights both hyphenated and slash-separated words in a cell with HTML styling.

        Parameters:
        - cell: The cell content to be processed.

        Returns:
        - The processed cell content with highlighted patterns.
        """
        # Highlight hyphenated words
        hyphenated_highlight_re = r'\b\w+(?:-\w+)+\b'
        # Highlight slash separated words
        slash_highlight_pattern = r'\b\w+(?:/\w+)+\b'
        # Highlight combinations of hyphenated and slash-separated words
        hyphenated_slash_combo_highlight = r'\b(\w+(?:-\w+)+/\w+|\w+/\w+(?:-\w+)+)\b'

        # Apply highlighting to combinations first to avoid overlap issues
        cell = re.sub(hyphenated_slash_combo_highlight,
                      lambda x: f"<span style='color: green;'><strong>{x.group()}</strong></span>", cell)

        # Apply highlighting to hyphenated words
        cell = re.sub(hyphenated_highlight_re,
                      lambda x: f"<span style='color: red;'><strong>{x.group()}</strong></span>", cell)

        # Apply highlighting to slash-separated words
        cell = re.sub(
            slash_highlight_pattern, lambda x: f"<span style='color: blue;'><strong>{x.group()}</strong></span>", cell)

        return cell
