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
        ['/', 'Introduction'] , 
        'apache', 
        'mysql', 
        'php' 
      ],
      '/raspberrypi-gpio/': [
        ['/raspberrypi-gpio/', 'Introduction'] , 
        'the_raspberry_pi', 
        'interfacing_hardware', 
        'gpio_interfacing', 
        'i2c_interfacing', 
        'spi_interfacing', 
        'serial_interfacing'
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
