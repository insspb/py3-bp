Issues and Pull request templates for Github and Gitlab sites
=============================================================

*Implemented in 0.0.4*

This template is compatible with `Github issues templates
<https://help.github.com/en/articles/creating-issue-templates-for-your-repository>`_
and `Gitlab description templates <https://docs.gitlab.com/ee/user/project/description_templates.html>`_
features.

During execution of this template you would be asked about templates
installation for popular version control systems:

* Install issues templates?

You can install templates for one of engines, by selecting relevant option,
or install templates for both systems, what is rarely required.

Default answer is ``no``, so templates would not be installed by default.

If you select ``Github`` or ``Gitlab`` related folder will be created. When
you select ``both`` both folders will be created, but it is rare case when
this is required.

* Github related templates will be located in generated project root, in
  ``.github`` hidden folder.
* Gitlab related templates will be located in generated project root, in
  ``.gitlab`` hidden folder.

Both folder contains almost similar issues and pull request templates, in
Markdown format, updated for Gitlab or Github requirements.

There is no option to select witch templates to install on generation phase,
so if you do not need some fo them - just delete related files before init
commit.

Included issue templates:

- Bug report
- Documentation report
- Enhancement request

Only general pull request included.
