#cfn-yaml:
#YAML CloudFormation Template Snippet Set for Sublime Text 3


cfn-yaml is a sublime text 3 package of snippets for cloudfront yaml syntax.

The snippet set is created from the AWS documentation as the master defintion for the YAML content and includes a comment within each snippet referencing back to the [AWS Reference documentation pages](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html) for easy right-click opening of the documentation related to the snippet.  This is obviously included to make it quick and easy to get back to the documentation related to the function being configured.

To activate snippets once installed, simply ensure your document type is set to YAML or CloudFormation (CForm) and type cfn.

This snippet set was inspired by cform package that provides a full snippet set for json based cloudformation APIs.

Should you wish to remove the documentation links after you've finished creating your template, then simply do a search and replace with regex enabled finding `#AWS-DOC.*\n` and replace with `nothing`

```
Usage:

# Easiest way to get to use these snippets is simply to clone this repo into your 
# Sublime Text 3 User Packages folder.

cd ~/.config/sublime-text-3/Packages/User
git clone https://github.com/Narrowbeam/cfn-yaml.git
```
Please note that these are still a work in progress and will evolve over time to include inter-field tabbing support (see Todo Issues)

If you find any issues or want to expand the snippet set, just create a pull request :-)