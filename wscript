# -*- mode: python -*-

def common(ctx):
    ctx.default_sdk = "10.4"
    ctx.default_compiler = "gcc"
    ctx.load("compiler_c compiler_cxx")
    ctx.load("core externals", "ext/waf-sfiera")
    ctx.external("libsfz")

def options(opt):
    common(opt)

def configure(cnf):
    common(cnf)
    cnf.check(lib="z", uselib_store="libzipxx/system/libz")

def build(bld):
    common(bld)

    bld.stlib(
        target="libzipxx/libzipxx",
        features="universal",
        source="src/zipxx/Zip.cpp",
        cxxflags="-Wall -Werror",
        includes="./include",
        export_includes="./include",
        use=[
            "libsfz/libsfz",
            "libzipxx/libzip",
        ],
    )

    bld.stlib(
        target="libzipxx/libzip",
        features="universal",
        source=[
            "libzip-0.9.3/lib/mkstemp.c",
            "libzip-0.9.3/lib/zip_add.c",
            "libzip-0.9.3/lib/zip_add_dir.c",
            "libzip-0.9.3/lib/zip_close.c",
            "libzip-0.9.3/lib/zip_delete.c",
            "libzip-0.9.3/lib/zip_dirent.c",
            "libzip-0.9.3/lib/zip_entry_free.c",
            "libzip-0.9.3/lib/zip_entry_new.c",
            "libzip-0.9.3/lib/zip_err_str.c",
            "libzip-0.9.3/lib/zip_error.c",
            "libzip-0.9.3/lib/zip_error_clear.c",
            "libzip-0.9.3/lib/zip_error_get.c",
            "libzip-0.9.3/lib/zip_error_get_sys_type.c",
            "libzip-0.9.3/lib/zip_error_strerror.c",
            "libzip-0.9.3/lib/zip_error_to_str.c",
            "libzip-0.9.3/lib/zip_fclose.c",
            "libzip-0.9.3/lib/zip_file_error_clear.c",
            "libzip-0.9.3/lib/zip_file_error_get.c",
            "libzip-0.9.3/lib/zip_file_get_offset.c",
            "libzip-0.9.3/lib/zip_file_strerror.c",
            "libzip-0.9.3/lib/zip_filerange_crc.c",
            "libzip-0.9.3/lib/zip_fopen.c",
            "libzip-0.9.3/lib/zip_fopen_index.c",
            "libzip-0.9.3/lib/zip_fread.c",
            "libzip-0.9.3/lib/zip_free.c",
            "libzip-0.9.3/lib/zip_get_archive_comment.c",
            "libzip-0.9.3/lib/zip_get_archive_flag.c",
            "libzip-0.9.3/lib/zip_get_file_comment.c",
            "libzip-0.9.3/lib/zip_get_name.c",
            "libzip-0.9.3/lib/zip_get_num_files.c",
            "libzip-0.9.3/lib/zip_memdup.c",
            "libzip-0.9.3/lib/zip_name_locate.c",
            "libzip-0.9.3/lib/zip_new.c",
            "libzip-0.9.3/lib/zip_open.c",
            "libzip-0.9.3/lib/zip_rename.c",
            "libzip-0.9.3/lib/zip_replace.c",
            "libzip-0.9.3/lib/zip_set_archive_comment.c",
            "libzip-0.9.3/lib/zip_set_archive_flag.c",
            "libzip-0.9.3/lib/zip_set_file_comment.c",
            "libzip-0.9.3/lib/zip_set_name.c",
            "libzip-0.9.3/lib/zip_source_buffer.c",
            "libzip-0.9.3/lib/zip_source_file.c",
            "libzip-0.9.3/lib/zip_source_filep.c",
            "libzip-0.9.3/lib/zip_source_free.c",
            "libzip-0.9.3/lib/zip_source_function.c",
            "libzip-0.9.3/lib/zip_source_zip.c",
            "libzip-0.9.3/lib/zip_stat.c",
            "libzip-0.9.3/lib/zip_stat_index.c",
            "libzip-0.9.3/lib/zip_stat_init.c",
            "libzip-0.9.3/lib/zip_strerror.c",
            "libzip-0.9.3/lib/zip_unchange.c",
            "libzip-0.9.3/lib/zip_unchange_all.c",
            "libzip-0.9.3/lib/zip_unchange_archive.c",
            "libzip-0.9.3/lib/zip_unchange_data.c",
        ],
        includes="./libzip-0.9.3/lib",
        export_includes="./libzip-0.9.3/lib",
        use=[
            "libzipxx/system/libz",
        ],   
    )

    bld.platform(
        target="libzipxx/libzip",
        platform="darwin",
        includes="./config/mac",
    )

    bld.platform(
        target="libzipxx/libzip",
        platform="linux",
        includes="./config/linux",
    )

    def program(name):
        bld.program(
            target="libzipxx/%s" % name,
            features="universal",
            source="libzip-0.9.3/src/%s.c" % name,
            includes="./config/mac",
            use=[
                "libzipxx/libzip",
            ],
        )

    program("zipcmp")
    # program("zipmerge")
    program("ziptorrent")
