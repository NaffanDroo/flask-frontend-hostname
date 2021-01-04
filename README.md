# flask-frontend-hostname
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
Front end for `flask-backend-hostname`.

In the azure-pipelines.yml update the `azdo-gcp-dev` with your google  
project name.

This application has a dependency on the `flask-backend-hostname`  
service.

It will try and connect to the kubernetes service named  
`backend-service` within the same namespace.

If it cannot detect the `POD_NAMESPACE` environment variable as defined
in the [deployment.yaml](deployment.yaml) then it will default to:
`http://localhost:5000` for the purposes of local development.
## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="http://www.nathandrew.org"><img src="https://avatars1.githubusercontent.com/u/1035229?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Nathan Drew</b></sub></a><br /><a href="https://github.com/NaffanDroo/flask-frontend-hostname/commits?author=NaffanDroo" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!