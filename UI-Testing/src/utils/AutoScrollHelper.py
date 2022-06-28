from selenium.webdriver.support.ui import WebDriverWait

class AutoScrollHelper:
    
    def __init__(self, driver, navbarHeight, footerHeight) -> None:
        self.driver =  driver
        self.navbarHeight = navbarHeight
        self.footerHeight = footerHeight

    def scrollTo(self, webElement):
        self.driver.execute_script(
            '\
            (function (global, element, navbarHeigth, footerHeigth) {\
                const _navbarHeigth = navbarHeigth || 0;\
                const _footerHeigth = footerHeigth || 0;\
            \
              autoScrollTo(element);\
            \
              function autoScrollTo(element) {\
                const elementPositionInfo = getElementPositionInfo(element);\
            \
                if (elementPositionInfo.isInTheViewport) return;\
            \
                global.scrollTo({\
                  top: calculateY(elementPositionInfo),\
                  left: calculateX(elementPositionInfo)\
                });\
              };\
            \
              function getElementPositionInfo(element) {\
                const bounding = element.getBoundingClientRect();\
                const isBelowTheViewport = bounding.bottom > (global.innerHeight - _footerHeigth || document.documentElement.clientHeight - _footerHeigth);\
                const isAboveViewPort = bounding.top < 0 || bounding.top < _navbarHeigth;\
                const isAtTheRight = bounding.right > (global.innerWidth || document.documentElement.clientWidth);\
                const isAtTheLeft = bounding.left < 0;\
                const isInTheViewport = !isBelowTheViewport && !isAboveViewPort && !isAtTheRight && !isAtTheLeft;\
            \
                return {\
                  bounding: bounding,\
                  isBelowTheViewport: isBelowTheViewport,\
                  isAboveViewPort: isAboveViewPort,\
                  isAtTheRight: isAtTheRight,\
                  isAtTheLeft: isAtTheLeft,\
                  isInTheViewport: isInTheViewport,\
                };\
              };\
            \
             function calculateY(elementPositionInfo) {\
                let currentYPosition = global.pageYOffset;\
            \
                if (elementPositionInfo.isBelowTheViewport)\
                  return elementPositionInfo.bounding.y + currentYPosition - _navbarHeigth;\
            \
                if (elementPositionInfo.isAboveViewPort)\
                  return currentYPosition + elementPositionInfo.bounding.y - _navbarHeigth;\
            \
                return currentYPosition;\
              };\
            \
              function calculateX(elementPositionInfo) {\
                let currentXPosition = global.pageXOffset;\
            \
                if (elementPositionInfo.isAtTheRight)\
                  return elementPositionInfo.bounding.x + currentXPosition;\
            \
                if (elementPositionInfo.isAtTheLeft)\
                  return currentXPosition + elementPositionInfo.bounding.x;\
            \
                return currentXPosition;\
              };\
            })(window, arguments[0], arguments[1], arguments[2]);',
            webElement,
            self.navbarHeight,
            self.footerHeight)

        wait = WebDriverWait(self.driver, 30)
        wait.until(lambda driver:  self.isInTheViewport(webElement))


    def isInTheViewport(self, webElement):
        return self.driver.execute_script(
            'return isInTheViewport(arguments[0], arguments[1], arguments[2]);\
            \
            function isInTheViewport(element, navbarHeigth, footerHeigth) {\
            const _navbarHeigth = navbarHeigth || 0;\
            const _footerHeigth = footerHeigth || 0;\
            \
            const bounding = element.getBoundingClientRect();\
            const isBelowTheViewport = bounding.bottom > (window.innerHeight - _footerHeigth || document.documentElement.clientHeight - _footerHeigth);\
            const isAboveViewPort = bounding.top < 0 || bounding.top < _navbarHeigth;\
            const isAtTheRight = bounding.right > (window.innerWidth || document.documentElement.clientWidth);\
            const isAtTheLeft = bounding.left < 0;\
            const isInTheViewport = !isBelowTheViewport && !isAboveViewPort && !isAtTheRight && !isAtTheLeft;\
            \
            return isInTheViewport;\
            };',
            webElement,
            self.navbarHeight,
            self.footerHeight)