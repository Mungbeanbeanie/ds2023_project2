"""Shared colors and chart styling. Import it so every chart matches the brand guide."""
# UVA colors
NAVY, GRAY, ORANGE, PEACH, WHITE = "#232D4B", "#C9CBD2", "#E57200", "#F9DCBE", "#FFFFFF"

# Chart roles
HIGHLIGHT, MUTED_MARK, TEXT, TEXT_SOFT = ORANGE, GRAY, NAVY, "#4A5677"
PAGE, GRID, NEUTRAL = "#F6F6F8", "#E4E5EA", "#F1F1F3"
NAVY_RAMP = ["#A3ABC2", "#7782A0", "#4A5677", "#232D4B"]           # ordered groups, low to high
DIVERGING = [[0, ORANGE], [0.5, NEUTRAL], [1, NAVY]]                # below usual -> above usual
FONT = "Libre Franklin, Franklin Gothic, Arial, sans-serif"


def style_plotly(fig):
    fig.update_layout(template="none", font=dict(family=FONT, color=TEXT, size=13),
                      paper_bgcolor=WHITE, plot_bgcolor=WHITE, colorway=NAVY_RAMP[::-1])
    fig.update_xaxes(gridcolor=GRID, zeroline=False)
    fig.update_yaxes(gridcolor=GRID, zeroline=False)
    return fig


# Usage: plt.rcParams.update(MATPLOTLIB)
MATPLOTLIB = {"font.family": ["Libre Franklin", "Arial", "DejaVu Sans"], "text.color": TEXT,
              "axes.labelcolor": TEXT_SOFT, "xtick.color": TEXT_SOFT, "ytick.color": TEXT,
              "axes.edgecolor": GRID, "axes.spines.top": False, "axes.spines.right": False,
              "grid.color": GRID, "figure.facecolor": WHITE, "axes.facecolor": WHITE}
