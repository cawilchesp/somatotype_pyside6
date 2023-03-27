def colors(theme: bool, role: str) -> str:
    light = {
        'background': '#eceff4',
        'on_background': '#001f2a',
        'surface_tint': '#d8dee9',
        'surface': '#eceff4',
        'on_surface': '#001f2a',

        'outline': '#2e3440',

        'primary': '#5e81ac',
        'on_primary': '#2e3440',
        'secondary': '#81a1c1',
        'on_secondary': '#2e3440',

        'hover': '#88c0d0',
        'disable': '#dfe2eb',
        'on_disable': '#43474e',

        'error': '#ba1a1a',
        'error_container': '#ffdad6',
        'on_error': '#ffffff',
        'on_error_container': '#410002',
    }

    dark = {
        'background': '#2e3440',
        'on_background': '#bfe9ff',
        'surface_tint': '#4c566a',
        'surface': '#2e3440',
        'on_surface': '#bfe9ff',

        'outline': '#d8dee9',

        'primary': '#81a1c1',
        'on_primary': '#eceff4',
        'secondary': '#5e81ac',
        'on_secondary': '#eceff4',

        'hover': '#88c0d0',
        'disable': '#43474e',
        'on_disable': '#dfe2eb',

        'error': '#ffb4ab',
        'error_container': '#93000a',
        'on_error': '#690005',
        'on_error_container': '#ffdad6',
    }

    if theme:
        return light[role]
    else:
        return dark[role]