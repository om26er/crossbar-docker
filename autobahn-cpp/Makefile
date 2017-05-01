SUBDIRS = x86_64 armhf aarch64

subdirs: $(SUBDIRS)

BUILDDIRS = $(SUBDIRS:%=build-%)
BUILDGCCDIRS = $(SUBDIRS:%=build-gcc-%)
BUILDCLANGDIRS = $(SUBDIRS:%=build-clang-%)
VERSIONDIRS = $(SUBDIRS:%=version-%)
TESTDIRS = $(SUBDIRS:%=test-%)
PUBLISHDIRS = $(SUBDIRS:%=publish-%)

build: $(BUILDDIRS)
build_gcc: $(BUILDGCCDIRS)
build_clang: $(BUILDCLANGDIRS)
version: $(VERSIONDIRS)
test: $(TESTDIRS)
publish: $(PUBLISHDIRS)

.PHONY: subdirs $(BUILDDIRS) $(BUILDGCCDIRS) $(BUILDCLANGDIRS) $(VERSIONDIRS) $(TESTDIRS) $(PUBLISHDIRS)
.PHONY: build version test publish

$(BUILDDIRS):
	$(MAKE) -C $(@:build-%=%) build

$(BUILDGCCDIRS):
	$(MAKE) -C $(@:build-gcc-%=%) build_gcc

$(BUILDCLANGDIRS):
	$(MAKE) -C $(@:build-clang-%=%) build_clang

$(VERSIONDIRS):
	$(MAKE) -C $(@:version-%=%) version

$(TESTDIRS):
	$(MAKE) -C $(@:test-%=%) test

$(PUBLISHDIRS):
	$(MAKE) -C $(@:publish-%=%) publish

list:
	docker images crossbario/autobahn-cpp*:*

clean:
	./removeall.sh
