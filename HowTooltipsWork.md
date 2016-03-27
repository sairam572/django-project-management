# Introduction #

Design decision: Put the power to update the definitions and help text in the hands of the project manager, not the developer.

# Details #

When a user hovers over a form element (i.e. a text box describing a project deliverable) they are presented with a popup message giving them some basic help.

The ExtJS element has a custom property that was defined in new\_site\_media/js/main-ui.js (in [r241](https://code.google.com/p/django-project-management/source/detail?r=241) this is on line 55. This defines 2 attributes on a ExtJS form element

  * ttEnabled: true/false
  * cmsSlug: string

This indicates whether ExtJS should attempt to load a popup for the element and if so which string to load.

This text is loaded via AJAX using the URL `/GetDoc`. An example call would be `/GetDoc?field=deliverable-rpo`

The Django view function that handles the request for documentation strings (project.views.get\_doc) looks for the correct `DjangoCMS` page (or actually the `PageContent` model) and returns it back to the user interface as a string.