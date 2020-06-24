(function () {
    // Retrieve previous config object if defined
    window.PagedConfig = window.PagedConfig || {};
    let beforePaged = window.PagedConfig.before;
    window.PagedConfig.before = async () => {
        if (beforePaged) await beforePaged();
        return new Promise((resolve, reject) => {
            var script = document.createElement("script");
            script.type = "text/javascript";
            var src = `https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js`;
            if (location.protocol !== "file:" && /^https?:/.test(src))
                src = src.replace(/^https?:/, '');
            script.src = src;
            window.MathJax = {
                tex: {
                    inlineMath: [['\\(','\\)']],
                    displayMath: [['\\[','\\]']],
                    processEscapes: true,
                    processEnvironments: true,
                    autoload: {
                      color: [],
                      colorV2: ['color']
                    },
                    packages: {'[+]': ['noerrors']}
                },
                options: {
                  skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre'],
                  ignoreHtmlClass: 'tex2jax_ignore',
                  processHtmlClass: 'tex2jax_process'
                },
                loader: {
                  load: ['input/asciimath', '[tex]/noerrors']
                },
                startup: {
                    ready: () => {
                        MathJax.startup.defaultReady();
                        MathJax.startup.promise.then(resolve);
                    }
                }
            };
            document.head.appendChild(script);
        });
    };
})();