module.exports = {
  title: 'git-pyhton-pi-web',
  description: '',
  themeConfig: {
    nav: [
      {text: 'VIVES', link: 'https://www.vives.be'}
    ],
    displayAllHeaders: true,
    sidebar: 'auto',
    repo: 'VIVES-Elektronica-ICT-Brugge/git-python-pi-web',
    docsDir: 'docs',
    docsBranch: 'master',
    editLinks: true,
    editLinkText: 'Edit this page!',
    sidebar: {
      '/lamp-server/': [
        ['/lamp-server/', 'Introduction'] , 
        'apache', 
        'mysql', 
        'php' 
      ],

      '/': [
        // '',
        '/git-and-github/',
        '/python/',
        '/raspberrypi-gpio/',
        '/lamp-server/'
      ]
    }
  },
  markdown: {
    lineNumbers: true,
  },
  serviceWorker: true,
}
