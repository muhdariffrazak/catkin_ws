
(cl:in-package :asdf)

(defsystem "assignments-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "MapFilePath" :depends-on ("_package_MapFilePath"))
    (:file "_package_MapFilePath" :depends-on ("_package"))
  ))