#cfn-yaml:
#YAML CloudFormation Template Snippet Set for Sublime Text 3


cfn-yaml is a sublime text 3 package of snippets for cloudfront yaml syntax.

The snippet set is created from the AWS documentation as the master defintion for the YAML content and includes a comment within each snippet referencing back to the [AWS Reference documentation pages](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html) for easy right-click opening of the documentation related to the snippet.  This is obviously included to make it quick and easy to get back to the documentation related to the function being configured.

To activate snippets once installed, simply ensure your document type is set to YAML or CloudFormation (CForm) and type cfn.

This snippet set was inspired by cform package that provides a full snippet set for json based cloudformation APIs.

Should you wish to remove the documentation links after you've finished creating your template, then simply do a search and replace with regex enabled finding `# AWS-DOC.*\n` and replace with `nothing`

```
Usage:

# Easiest way to get to use these snippets is simply to clone this repo into your 
# Sublime Text 3 User Packages folder.

cd ~/.config/sublime-text-3/Packages/User
git clone https://github.com/Narrowbeam/cfn-yaml.git
```
Please note that while this was a work in progress, it does provide a fairly full set of snippets.  Since I created this collection, i've taken the decision for various reasons to migrate towards vscode as my default editor, so won't be updating this repo going forwards.  I may however write a more generic snippet generator for aws resources following AWS releasing the resource api spec in machine readable json format.  No more crawling the documentation set to build the snippets.  If I do this, I will produce snippets for sublime as well as vscode; Until then, hope this remains fairly up to date.

If you find any issues or want to expand the snippet set, just create a pull request :-)
