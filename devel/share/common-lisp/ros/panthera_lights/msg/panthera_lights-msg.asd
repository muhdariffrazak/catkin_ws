
(cl:in-package :asdf)

(defsystem "panthera_lights-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "LightStatus" :depends-on ("_package_LightStatus"))
    (:file "_package_LightStatus" :depends-on ("_package"))
  ))